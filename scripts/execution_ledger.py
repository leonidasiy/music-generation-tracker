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
    return SENSITIVE_LABEL.sub(lambda match: f"{match.group(1)}: [REDACTED]", text)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def describe_outputs(paths: Iterable[Path]) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    for raw_path in paths:
        path = raw_path.expanduser().resolve()
        if not path.exists():
            records.append({"path": str(path), "exists": False})
            continue
        record: dict[str, object] = {
            "path": str(path),
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
        ledger = json.loads(ledger_path.read_text(encoding="utf-8"))
    else:
        ledger = {"schema_version": 1, "updated_at": timestamp, "entries": []}

    existing = ledger.get("entries", [])
    sequence = len(existing) + 1
    compact_time = timestamp.replace("-", "").replace(":", "")
    entry_id = f"{compact_time}-{sequence:03d}"
    normalized_outputs = (
        describe_outputs(outputs) if outputs and isinstance(outputs[0], Path) else outputs
    )
    entry = {
        "id": entry_id,
        "timestamp": timestamp,
        "phase": phase,
        "title": title,
        "status": status,
        "cwd": str(Path(cwd).expanduser().resolve()),
        "command": redact(command),
        "exit_code": exit_code,
        "output_summary": redact(output_summary[-4000:]),
        "outputs": normalized_outputs,
    }
    existing.append(entry)
    ledger["entries"] = existing
    ledger["updated_at"] = timestamp
    ledger["current_status"] = title
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
