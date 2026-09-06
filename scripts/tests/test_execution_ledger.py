import json
import tempfile
import unittest
from pathlib import Path

from execution_ledger import append_entry, public_path, run_logged_command


class ExecutionLedgerTests(unittest.TestCase):
    def setUp(self):
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        self.ledger = self.root / "execution-log.json"

    def test_public_path_hides_host_layout(self):
        self.assertEqual(public_path(self.root, self.root), ".")
        self.assertEqual(public_path(self.root / "outputs" / "result.json", self.root), "outputs/result.json")
        self.assertEqual(public_path(Path("/private/tmp/external.mid"), self.root), "[external]/external.mid")

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
        self.assertEqual(data["entries"][0]["cwd"], ".")
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

    def test_literal_and_url_encoded_home_paths_are_redacted_everywhere(self):
        home = "/Users/example/.hermes/profiles/researcher/private.mid"
        encoded = "%2FUsers%2Fexample%2F.cache%2Fprivate.mid"
        append_entry(
            self.ledger,
            phase="test",
            title=f"Inspect {home}",
            status="completed",
            cwd=self.root,
            command=f"inspect {home} {encoded}",
            exit_code=0,
            output_summary=f"server_result.file={encoded}",
            outputs=[{
                "path": home,
                "nested": {
                    f"literal-key:{home}": "safe",
                    f"encoded-key:{encoded}": "safe",
                },
            }],
            timestamp="2026-07-17T09:31:30Z",
        )
        text = self.ledger.read_text()
        self.assertNotIn("/Users/example", text)
        self.assertNotIn("%2FUsers%2Fexample", text)
        self.assertNotIn(".hermes/profiles/researcher", text)
        self.assertIn("[PROFILE]", text)
        self.assertIn("%5BHOME%5D", text)
        nested = json.loads(text)["entries"][0]["outputs"][0]["nested"]
        self.assertEqual(
            nested,
            {
                "literal-key:[PROFILE]/private.mid": "safe",
                "encoded-key:%5BHOME%5D%2F.cache%2Fprivate.mid": "safe",
            },
        )

    def test_ledger_does_not_publish_a_stale_hash_of_itself(self):
        append_entry(
            self.ledger,
            phase="test",
            title="Self reference",
            status="completed",
            cwd=self.root,
            command="update ledger",
            exit_code=0,
            output_summary="ok",
            outputs=[self.ledger],
            timestamp="2026-07-17T09:32:00Z",
        )
        output = json.loads(self.ledger.read_text())["entries"][0]["outputs"][0]
        self.assertEqual(output["kind"], "ledger-self-reference")
        self.assertNotIn("sha256", output)
        self.assertNotIn("size_bytes", output)

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
        self.assertEqual(record["outputs"][0]["path"], "artifact.txt")
        self.assertEqual(record["outputs"][0]["size_bytes"], 2)
        self.assertEqual(len(record["outputs"][0]["sha256"]), 64)


if __name__ == "__main__":
    unittest.main()
