#!/usr/bin/env python3
"""Execute and record reproducible project steps in a public JSON ledger."""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import subprocess
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

SENSITIVE_ASSIGNMENT = re.compile(
    r"(?i)\b(api[_-]?key|token|secret|password|passwd|authorization)\s*=\s*(?:'[^']*'|\"[^\"]*\"|\S+)"
)
SENSITIVE_FLAG = re.compile(
    r"(?i)(--(?:api[_-]?key|token|secret|password|passwd|authorization)(?:=|\s+))(?:'[^']*'|\"[^\"]*\"|\S+)"
)
SENSITIVE_LABEL = re.compile(
    r"(?i)\b(api[_-]?key|token|secret|password|passwd|authorization)\s*:\s*\S+"
)
LOCAL_HOME = re.compile(r"(?i)(?:/Users/|/home/)[^/\s\"'<>?&]+")
ENCODED_LOCAL_HOME = re.compile(
    r"(?i)%2f(?:Users|home)%2f(?:(?!%2f|[\s\"'<>?&]).)+"
)
LOCAL_PROFILE = re.compile(r"(?i)\[HOME\]/\.hermes/profiles/[^/\s\"'<>?&]+")
ENCODED_LOCAL_PROFILE = re.compile(
    r"(?i)%5bHOME%5d%2f\.hermes%2fprofiles%2f(?:(?!%2f|[\s\"'<>?&]).)+"
)


@dataclass(frozen=True)
class CommandResult:
    returncode: int
    stdout: str
    stderr: str


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def redact(text: str) -> str:
    text = SENSITIVE_ASSIGNMENT.sub(lambda match: f"{match.group(1)}=[REDACTED]", text)
    text = SENSITIVE_FLAG.sub(lambda match: f"{match.group(1)}[REDACTED]", text)
    text = SENSITIVE_LABEL.sub(lambda match: f"{match.group(1)}: [REDACTED]", text)
    text = ENCODED_LOCAL_HOME.sub("%5BHOME%5D", text)
    text = LOCAL_HOME.sub("[HOME]", text)
    text = ENCODED_LOCAL_PROFILE.sub("%5BPROFILE%5D", text)
    return LOCAL_PROFILE.sub("[PROFILE]", text)


def redact_value(value):
    """Recursively sanitize every public string, including output records."""
    if isinstance(value, str):
        return redact(value)
    if isinstance(value, list):
        return [redact_value(item) for item in value]
    if isinstance(value, dict):
        return {redact_value(key): redact_value(item) for key, item in value.items()}
    return value


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def public_path(path: Path, root: Path) -> str:
    """Render a ledger path without exposing the host's home/profile layout."""
    path = path.expanduser().resolve()
    root = root.expanduser().resolve()
    try:
        relative = path.relative_to(root)
    except ValueError:
        return f"[external]/{path.name}"
    return "." if relative == Path(".") else relative.as_posix()


def describe_outputs(
    paths: Iterable[Path], ledger_path: Path | None = None
) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for raw_path in paths:
        path = raw_path.expanduser().resolve()
        root = ledger_path.expanduser().resolve().parent if ledger_path is not None else Path.cwd().resolve()
        display_path = public_path(path, root)
        if ledger_path is not None and path == ledger_path.expanduser().resolve():
            records.append(
                {"path": display_path, "exists": path.exists(), "kind": "ledger-self-reference"}
            )
            continue
        if not path.exists():
            records.append({"path": display_path, "exists": False})
            continue
        record: dict[str, object] = {
            "path": display_path,
            "exists": True,
            "kind": "directory" if path.is_dir() else "file",
        }
        if path.is_file():
            record["size_bytes"] = path.stat().st_size
            record["sha256"] = sha256_file(path)
        records.append(record)
    return records


def append_entry(
    ledger_path: Path,
    *,
    phase: str,
    title: str,
    status: str,
    cwd: Path,
    command: str,
    exit_code: int | None,
    output_summary: str,
    outputs: list[dict[str, object]] | list[Path],
    timestamp: str | None = None,
) -> dict[str, object]:
    timestamp = timestamp or utc_now()
    ledger_path = ledger_path.expanduser().resolve()
    if ledger_path.exists():
        ledger = redact_value(json.loads(ledger_path.read_text(encoding="utf-8")))
    else:
        ledger = {"schema_version": 1, "updated_at": timestamp, "entries": []}

    existing = ledger.get("entries", [])
    sequence = len(existing) + 1
    compact_time = timestamp.replace("-", "").replace(":", "")
    entry_id = f"{compact_time}-{sequence:03d}"
    normalized_outputs = (
        describe_outputs(outputs, ledger_path)
        if outputs and isinstance(outputs[0], Path)
        else outputs
    )
    entry = {
        "id": entry_id,
        "timestamp": timestamp,
        "phase": redact(phase),
        "title": redact(title),
        "status": redact(status),
        "cwd": public_path(Path(cwd), ledger_path.parent),
        "command": redact(command),
        "exit_code": exit_code,
        "output_summary": redact(output_summary[-4000:]),
        "outputs": redact_value(normalized_outputs),
    }
    existing.append(entry)
    ledger["entries"] = existing
    ledger["updated_at"] = timestamp
    ledger["current_status"] = entry["title"]
    ledger_path.parent.mkdir(parents=True, exist_ok=True)
    ledger_path.write_text(json.dumps(ledger, indent=2, sort_keys=False) + "\n", encoding="utf-8")
    return entry


def run_logged_command(
    *,
    ledger_path: Path,
    phase: str,
    title: str,
    cwd: Path,
    command: str,
    output_paths: Iterable[Path] = (),
    timeout: int | None = None,
) -> CommandResult:
    cwd = Path(cwd).expanduser().resolve()
    completed = subprocess.run(
        command,
        cwd=cwd,
        shell=True,
        text=True,
        capture_output=True,
        timeout=timeout,
        executable="/bin/bash",
    )
    combined = "\n".join(part for part in (completed.stdout.strip(), completed.stderr.strip()) if part)
    append_entry(
        ledger_path,
        phase=phase,
        title=title,
        status="completed" if completed.returncode == 0 else "failed",
        cwd=cwd,
        command=command,
        exit_code=completed.returncode,
        output_summary=combined,
        outputs=list(output_paths),
    )
    return CommandResult(completed.returncode, completed.stdout, completed.stderr)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--ledger", type=Path, default=Path("execution-log.json"))
    parser.add_argument("--phase", required=True)
    parser.add_argument("--title", required=True)
    parser.add_argument("--cwd", type=Path, default=Path.cwd())
    parser.add_argument("--output", action="append", type=Path, default=[])
    parser.add_argument("--timeout", type=int)
    parser.add_argument("command")
    args = parser.parse_args()

    result = run_logged_command(
        ledger_path=args.ledger,
        phase=args.phase,
        title=args.title,
        cwd=args.cwd,
        command=args.command,
        output_paths=args.output,
        timeout=args.timeout,
    )
    if result.stdout:
        print(result.stdout, end="")
    if result.stderr:
        print(result.stderr, end="", file=__import__("sys").stderr)
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
