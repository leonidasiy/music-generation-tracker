"""Deterministic Stage 0 utilities for CLPR experiment records."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any, Iterable, Mapping


class PromptRegistryError(ValueError):
    """Raised when the frozen prompt registry is malformed."""


class ManifestError(ValueError):
    """Raised when a run manifest is incomplete or inconsistent."""


_ALLOWED_REGION_CLASSES = {
    "target",
    "strict_preservation",
    "adaptation_allowed",
    "out_of_scope",
}
_ALLOWED_CONDITIONS = {"control", "intervention"}
_ALLOWED_SEED_STATUS = {"fixed", "random", "unavailable"}
_SHA256 = re.compile(r"^[0-9a-f]{64}$")


def load_json(path: str | Path) -> dict[str, Any]:
    with Path(path).open("r", encoding="utf-8") as handle:
        value = json.load(handle)
    if not isinstance(value, dict):
        raise ValueError(f"Expected a JSON object in {path}")
    return value


def sha256_file(path: str | Path, chunk_size: int = 1024 * 1024) -> str:
    digest = hashlib.sha256()
    with Path(path).open("rb") as handle:
        for chunk in iter(lambda: handle.read(chunk_size), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _require(mapping: Mapping[str, Any], fields: Iterable[str], context: str, error_type: type[ValueError]) -> None:
    missing = [field for field in fields if field not in mapping]
    if missing:
        raise error_type(f"{context} missing required fields: {', '.join(missing)}")


def validate_regions(
    regions: Any,
    duration_sec: float,
    *,
    require_full_coverage: bool = False,
    error_type: type[ValueError] = PromptRegistryError,
) -> None:
    if not isinstance(regions, list) or not regions:
        raise error_type("regions must be a non-empty list")
    if duration_sec <= 0:
        raise error_type("duration_sec must be positive")

    previous_end: float | None = None
    names: set[str] = set()
    for index, region in enumerate(regions):
        if not isinstance(region, dict):
            raise error_type(f"region {index} must be an object")
        _require(region, ("name", "class", "start_sec", "end_sec"), f"region {index}", error_type)
        name = region["name"]
        region_class = region["class"]
        start = region["start_sec"]
        end = region["end_sec"]
        if not isinstance(name, str) or not name:
            raise error_type(f"region {index} has an invalid name")
        if name in names:
            raise error_type(f"duplicate region name: {name}")
        names.add(name)
        if region_class not in _ALLOWED_REGION_CLASSES:
            raise error_type(f"region {name} has unsupported class: {region_class}")
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise error_type(f"region {name} boundaries must be numeric")
        if start < 0 or end <= start or end > duration_sec:
            raise error_type(f"region {name} lies outside duration or has non-positive length")
        if previous_end is not None:
            if start < previous_end:
                raise error_type(f"region {name} overlaps the preceding region")
            if require_full_coverage and start != previous_end:
                raise error_type(f"gap before region {name}")
        previous_end = end

    if require_full_coverage:
        if regions[0]["start_sec"] != 0:
            raise error_type("full-coverage regions must start at zero")
        if previous_end != duration_sec:
            raise error_type("full-coverage regions must end at duration_sec")


def validate_prompt_registry(registry: Mapping[str, Any]) -> None:
    _require(registry, ("schema_version", "scope", "durations", "pairs"), "registry", PromptRegistryError)
    if not isinstance(registry["durations"], dict) or not registry["durations"]:
        raise PromptRegistryError("durations must be a non-empty object")
    for key, duration in registry["durations"].items():
        if not isinstance(duration, dict):
            raise PromptRegistryError(f"duration {key} must be an object")
        _require(duration, ("duration_sec", "regions"), f"duration {key}", PromptRegistryError)
        if str(duration["duration_sec"]) != str(key):
            raise PromptRegistryError(f"duration key {key} does not match duration_sec")
        validate_regions(
            duration["regions"],
            duration["duration_sec"],
            require_full_coverage=True,
            error_type=PromptRegistryError,
        )

    if not isinstance(registry["pairs"], list) or not registry["pairs"]:
        raise PromptRegistryError("pairs must be a non-empty list")
    pair_ids: set[str] = set()
    for index, pair in enumerate(registry["pairs"]):
        if not isinstance(pair, dict):
            raise PromptRegistryError(f"pair {index} must be an object")
        _require(pair, ("id", "template", "clauses", "changed_field"), f"pair {index}", PromptRegistryError)
        if pair["id"] in pair_ids:
            raise PromptRegistryError(f"duplicate pair id: {pair['id']}")
        pair_ids.add(pair["id"])
        template = pair["template"]
        if not isinstance(template, str):
            raise PromptRegistryError(f"pair {pair['id']} template must be text")
        if template.count("{TARGET_CLAUSE}") != 1:
            raise PromptRegistryError(f"pair {pair['id']} must contain exactly one TARGET_CLAUSE placeholder")
        if template.count("{DURATION}") != 1:
            raise PromptRegistryError(f"pair {pair['id']} must contain exactly one DURATION placeholder")
        if template.count("{FORM_TIMING}") > 1:
            raise PromptRegistryError(f"pair {pair['id']} has multiple FORM_TIMING placeholders")
        clauses = pair["clauses"]
        if not isinstance(clauses, dict):
            raise PromptRegistryError(f"pair {pair['id']} clauses must be an object")
        _require(clauses, ("control", "intervention"), f"pair {pair['id']} clauses", PromptRegistryError)
        if not all(isinstance(clauses[c], str) and clauses[c].strip() for c in _ALLOWED_CONDITIONS):
            raise PromptRegistryError(f"pair {pair['id']} clauses must be non-empty text")
        if clauses["control"] == clauses["intervention"]:
            raise PromptRegistryError(f"pair {pair['id']} clauses must differ")
        if pair["changed_field"] != "target_clause":
            raise PromptRegistryError(f"pair {pair['id']} changed_field must be target_clause")


def render_prompt_pair(
    pair: Mapping[str, Any],
    duration_sec: int,
    *,
    form_timing: str | None = None,
) -> tuple[str, str]:
    template = pair["template"]
    if "{FORM_TIMING}" in template and not form_timing:
        raise PromptRegistryError("form_timing is required by this prompt template")
    shared = template.replace("{DURATION}", str(duration_sec))
    if form_timing is not None:
        shared = shared.replace("{FORM_TIMING}", form_timing)
    clauses = pair["clauses"]
    control = shared.replace("{TARGET_CLAUSE}", clauses["control"])
    intervention = shared.replace("{TARGET_CLAUSE}", clauses["intervention"])
    if "{" in control or "}" in control or "{" in intervention or "}" in intervention:
        raise PromptRegistryError("unresolved prompt placeholder")
    normalized_control = control.replace(clauses["control"], "<TARGET_CLAUSE>")
    normalized_intervention = intervention.replace(clauses["intervention"], "<TARGET_CLAUSE>")
    if normalized_control != normalized_intervention:
        raise PromptRegistryError("rendered prompts differ outside the target clause")
    return control, intervention


def validate_manifest(manifest: Mapping[str, Any]) -> None:
    _require(
        manifest,
        (
            "schema_version",
            "run_id",
            "pair_id",
            "condition",
            "generator",
            "generation",
            "environment",
            "output",
            "regions",
            "failures",
            "cost_usd",
            "cumulative_stage0_cost_usd",
            "created_at",
        ),
        "manifest",
        ManifestError,
    )
    if manifest["condition"] not in _ALLOWED_CONDITIONS:
        raise ManifestError(f"condition must be one of {sorted(_ALLOWED_CONDITIONS)}")
    if not isinstance(manifest["run_id"], str) or not manifest["run_id"]:
        raise ManifestError("run_id must be non-empty text")
    if not isinstance(manifest["pair_id"], str) or not manifest["pair_id"]:
        raise ManifestError("pair_id must be non-empty text")

    generator = manifest["generator"]
    if not isinstance(generator, dict):
        raise ManifestError("generator must be an object")
    _require(generator, ("name", "access_type", "version", "interface"), "generator", ManifestError)
    if not all(isinstance(generator[field], str) and generator[field] for field in ("name", "access_type", "version", "interface")):
        raise ManifestError("generator fields must be non-empty text")

    generation = manifest["generation"]
    if not isinstance(generation, dict):
        raise ManifestError("generation must be an object")
    _require(
        generation,
        ("submitted_prompt", "duration_requested_sec", "seed", "seed_status", "settings", "prompt_rewriting"),
        "generation",
        ManifestError,
    )
    if generation["seed_status"] not in _ALLOWED_SEED_STATUS:
        raise ManifestError(f"seed_status must be one of {sorted(_ALLOWED_SEED_STATUS)}")
    if generation["seed_status"] == "fixed" and not isinstance(generation["seed"], int):
        raise ManifestError("a fixed seed must be an integer")
    if not isinstance(generation["settings"], dict):
        raise ManifestError("generation.settings must be an object")
    if not isinstance(generation["prompt_rewriting"], bool):
        raise ManifestError("generation.prompt_rewriting must be boolean")

    output = manifest["output"]
    if not isinstance(output, dict):
        raise ManifestError("output must be an object")
    _require(
        output,
        ("path", "sha256", "duration_observed_sec", "sample_rate_hz", "channels", "size_bytes"),
        "output",
        ManifestError,
    )
    if not isinstance(output["sha256"], str) or not _SHA256.fullmatch(output["sha256"]):
        raise ManifestError("output.sha256 must be 64 lowercase hexadecimal characters")
    if output["duration_observed_sec"] <= 0 or output["sample_rate_hz"] <= 0 or output["channels"] <= 0 or output["size_bytes"] <= 0:
        raise ManifestError("output numeric fields must be positive")

    requested_duration = generation["duration_requested_sec"]
    if not isinstance(requested_duration, (int, float)) or requested_duration <= 0:
        raise ManifestError("duration_requested_sec must be positive")
    validate_regions(manifest["regions"], requested_duration, error_type=ManifestError)

    if not isinstance(manifest["failures"], list):
        raise ManifestError("failures must be a list")
    for field in ("cost_usd", "cumulative_stage0_cost_usd"):
        value = manifest[field]
        if not isinstance(value, (int, float)) or value < 0:
            raise ManifestError(f"{field} must be non-negative")
    if manifest["cumulative_stage0_cost_usd"] > 100:
        raise ManifestError("cumulative Stage 0 cost exceeds the hard $100 ceiling")


def _main() -> int:
    parser = argparse.ArgumentParser(description="Validate CLPR Stage 0 JSON artifacts")
    subparsers = parser.add_subparsers(dest="command", required=True)
    registry_parser = subparsers.add_parser("registry")
    registry_parser.add_argument("path")
    manifest_parser = subparsers.add_parser("manifest")
    manifest_parser.add_argument("path")
    hash_parser = subparsers.add_parser("sha256")
    hash_parser.add_argument("path")
    args = parser.parse_args()
    if args.command == "registry":
        validate_prompt_registry(load_json(args.path))
        print("registry valid")
    elif args.command == "manifest":
        validate_manifest(load_json(args.path))
        print("manifest valid")
    else:
        print(sha256_file(args.path))
    return 0


if __name__ == "__main__":
    raise SystemExit(_main())
