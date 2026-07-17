#!/usr/bin/env python3
"""Submit and archive one deterministic ACE-Step Stage 0 smoke-test generation."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


def request_json(url: str, payload: dict[str, Any], timeout: int = 30) -> dict[str, Any]:
    """POST JSON and return the decoded object."""
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.load(response)


def sha256_file(path: Path) -> str:
    """Return the SHA-256 digest for a local file."""
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main() -> int:
    """Run one generation, poll completion, download audio, and save metadata."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="http://127.0.0.1:8001")
    parser.add_argument("--output", required=True)
    parser.add_argument("--duration", type=float, default=10.0)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument(
        "--prompt",
        default=(
            "instrumental electronic pop groove, monophonic synthesizer lead, "
            "electronic kick, snare, closed hi-hat, bass and pads, no vocals"
        ),
    )
    parser.add_argument("--timeout", type=int, default=900)
    args = parser.parse_args()

    payload = {
        "prompt": args.prompt,
        "lyrics": "",
        "thinking": False,
        "sample_mode": False,
        "use_format": False,
        "use_cot_caption": False,
        "use_cot_language": False,
        "use_cot_metas": False,
        "bpm": 120,
        "key_scale": "C Major",
        "time_signature": "4",
        "audio_duration": args.duration,
        "audio_format": "flac",
        "model": "acestep-v15-turbo",
        "inference_steps": 8,
        "infer_method": "ode",
        "batch_size": 1,
        "use_random_seed": False,
        "seed": args.seed,
    }
    submitted_at = time.time()
    submission = request_json(f"{args.base_url}/release_task", payload, timeout=60)
    if submission.get("code") != 200:
        raise RuntimeError(f"submission failed: {submission}")
    task_id = submission["data"]["task_id"]

    deadline = time.monotonic() + args.timeout
    task: dict[str, Any] | None = None
    while time.monotonic() < deadline:
        query = request_json(
            f"{args.base_url}/query_result",
            {"task_id_list": [task_id]},
            timeout=min(args.timeout, 300),
        )
        records = query.get("data") or []
        if records:
            task = records[0]
            status = task.get("status")
            if status == 1:
                break
            if status == 2:
                raise RuntimeError(f"generation failed: {task}")
        time.sleep(5)
    else:
        raise TimeoutError(f"generation did not complete within {args.timeout}s")

    assert task is not None
    result_field = task.get("result")
    results = json.loads(result_field) if isinstance(result_field, str) else result_field
    if not results or results[0].get("status") != 1:
        raise RuntimeError(f"unexpected result payload: {results}")
    result = results[0]
    file_url = result["file"]
    if file_url.startswith("/"):
        file_url = f"{args.base_url}{file_url}"

    output = Path(args.output).expanduser().resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    with urllib.request.urlopen(file_url, timeout=120) as response:
        output.write_bytes(response.read())

    summary = {
        "task_id": task_id,
        "submitted_at_unix": submitted_at,
        "completed_at_unix": time.time(),
        "request": payload,
        "server_result": result,
        "output_path": str(output),
        "output_size_bytes": output.stat().st_size,
        "output_sha256": sha256_file(output),
    }
    summary_path = output.with_suffix(output.suffix + ".json")
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
