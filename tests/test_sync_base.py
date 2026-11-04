"""Synchronization contracts: detect drift without writing and copy BASE."""

import tempfile
import unittest
import subprocess
from pathlib import Path

from scripts.sync_base import SKILLS, sync_base


class SyncBaseTests(unittest.TestCase):
    def setUp(self):
        self.workspace = tempfile.TemporaryDirectory()
        self.addCleanup(self.workspace.cleanup)
        self.root = Path(self.workspace.name)
        (self.root / "BASE.md").write_text("test BASE\n", encoding="utf-8")
        for skill in SKILLS:
            (self.root / "skills" / skill).mkdir(parents=True)

    def test_check_reports_missing_copies_without_creating_them(self):
        self.assertEqual(len(sync_base(self.root)), 3)
        self.assertFalse(list(self.root.rglob("references")))

    def test_write_copies_exact_bytes_and_check_detects_later_drift(self):
        sync_base(self.root, write=True)
        for skill in SKILLS:
            target = self.root / "skills" / skill / "references" / "BASE.md"
            self.assertEqual(target.read_bytes(), (self.root / "BASE.md").read_bytes())
        self.assertEqual(sync_base(self.root), [])
        target.write_text("local change\n", encoding="utf-8")
        self.assertEqual(sync_base(self.root), [target])
        self.assertEqual(target.read_text(encoding="utf-8"), "local change\n")
        sync_base(self.root, write=True)
        self.assertEqual(sync_base(self.root), [])

    def test_missing_canonical_base_fails_before_writing(self):
        (self.root / "BASE.md").unlink()
        with self.assertRaises(FileNotFoundError):
            sync_base(self.root, write=True)
        self.assertFalse(list(self.root.rglob("references")))

    def test_cli_signals_drift_and_only_writes_when_requested(self):
        import sys

        script = self.root / "scripts" / "sync_base.py"
        script.parent.mkdir()
        source = Path(__file__).resolve().parents[1] / "scripts" / "sync_base.py"
        script.write_bytes(source.read_bytes())
        def run(*args):
            return subprocess.run(
                [sys.executable, str(script), *args],
                cwd=self.root, capture_output=True, text=True,
            )
        self.assertEqual(run().returncode, 1)
        self.assertFalse(list(self.root.rglob("references")))
        self.assertEqual(run("--write").returncode, 0)
        self.assertEqual(run().returncode, 0)


if __name__ == "__main__":
    unittest.main()
