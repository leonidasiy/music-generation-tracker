import json
import tempfile
import unittest
from pathlib import Path

from execution_ledger import append_entry, run_logged_command


class ExecutionLedgerTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.ledger = self.root / "execution-log.json"

    def tearDown(self):
        self.tempdir.cleanup()

    def test_append_entry_creates_deterministic_public_record(self):
        append_entry(
            self.ledger,
            phase="audit",
            title="Inspect repository",
            status="completed",
            cwd=self.root,
            command="git status --short",
            exit_code=0,
            output_summary="clean",
            outputs=[],
            timestamp="2026-07-17T09:30:00Z",
        )

        data = json.loads(self.ledger.read_text())
        self.assertEqual(data["updated_at"], "2026-07-17T09:30:00Z")
        self.assertEqual(data["entries"][0]["id"], "20260717T093000Z-001")
        self.assertEqual(data["entries"][0]["cwd"], str(self.root.resolve()))
        self.assertEqual(data["entries"][0]["command"], "git status --short")

    def test_sensitive_values_are_redacted(self):
        append_entry(
            self.ledger,
            phase="test",
            title="Redaction",
            status="completed",
            cwd=self.root,
            command="API_KEY=secret TOKEN='secret2' python run.py --password hunter2",
            exit_code=0,
            output_summary="token=leak password: leak2",
            outputs=[],
            timestamp="2026-07-17T09:31:00Z",
        )
        text = self.ledger.read_text()
        self.assertNotIn("secret", text)
        self.assertNotIn("hunter2", text)
        self.assertNotIn("leak2", text)
        self.assertIn("[REDACTED]", text)

    def test_run_logged_command_records_exit_and_created_output(self):
        output = self.root / "artifact.txt"
        result = run_logged_command(
            ledger_path=self.ledger,
            phase="test",
            title="Create artifact",
            cwd=self.root,
            command="python3 -c \"from pathlib import Path; Path('artifact.txt').write_text('ok')\"",
            output_paths=[output],
        )

        self.assertEqual(result.returncode, 0)
        record = json.loads(self.ledger.read_text())["entries"][0]
        self.assertEqual(record["exit_code"], 0)
        self.assertEqual(record["outputs"][0]["path"], str(output.resolve()))
        self.assertEqual(record["outputs"][0]["size_bytes"], 2)
        self.assertEqual(len(record["outputs"][0]["sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
