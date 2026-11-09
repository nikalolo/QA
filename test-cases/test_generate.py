"""Tooling checks in temporary copies; no application execution is performed."""
import csv
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest


class GeneratorSafety(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.home = Path(self.temp.name)
        self.repo = self.home / 'repo'
        shutil.copytree(Path(__file__).resolve().parent.parent, self.repo)
        self.source = self.repo / 'test-cases/test-cases.csv'

    def run_generator(self, *args):
        return subprocess.run([sys.executable, str(self.repo / 'test-cases/generate.py'), *args],
                              cwd=self.home, capture_output=True, text=True)

    def edit(self, change):
        with self.source.open(encoding='utf-8', newline='') as f:
            reader = csv.DictReader(f)
            fields, rows = reader.fieldnames, list(reader)
        change(rows)
        with self.source.open('w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=fields)
            writer.writeheader()
            writer.writerows(rows)

    def test_foreign_directory_idempotence_and_preserved_results(self):
        def change(rows):
            rows[0].update({'Status': 'PASS', 'Actual result': 'SYNTHETIC TOOLING FIXTURE ONLY',
                            'Design status': 'READY — requirement reviewed', 'Data used': 'fixture',
                            'Environment / date': 'fixture, not a real date', 'Notes / evidence': 'fixture'})
        self.edit(change)
        history = self.repo / 'test-cases/execution-log.csv'
        history.write_text('SYNTHETIC HISTORY SENTINEL\n', encoding='utf-8')
        before = {p: p.read_bytes() for p in self.repo.rglob('*') if p.is_file() and p.suffix != '.md'}
        result = self.run_generator()
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertFalse((self.home / 'test-cases.md').exists())
        for p, content in before.items():
            self.assertEqual(p.read_bytes(), content)
        self.assertEqual(self.run_generator('--check').returncode, 0)
        self.assertEqual(self.run_generator().returncode, 0)
        self.assertEqual(self.run_generator('--check').returncode, 0)

    def test_literal_html_pipes_and_newlines(self):
        self.edit(lambda rows: rows[0].update({'Test data': '<b>test</b> | a\nb *c*'}))
        self.assertEqual(self.run_generator().returncode, 0)
        md = (self.repo / 'test-cases/test-cases.md').read_text(encoding='utf-8')
        self.assertIn('&lt;b&gt;test&lt;/b&gt; &#124; a<br>b \\*c\\*', md)
        self.assertNotIn('<b>test</b>', md)

    def test_duplicate_rejected_before_output(self):
        self.edit(lambda rows: rows.append(rows[0].copy()))
        target = self.repo / 'test-cases/test-cases.md'
        before = target.read_bytes()
        self.assertNotEqual(self.run_generator().returncode, 0)
        self.assertEqual(target.read_bytes(), before)

    def test_bad_mapping_rejected(self):
        self.edit(lambda rows: rows[0].update({'Behaviour IDs': 'B-99'}))
        self.assertNotEqual(self.run_generator('--check').returncode, 0)

    def test_verdict_without_evidence_fields_rejected(self):
        self.edit(lambda rows: rows[0].update({'Status': 'PASS', 'Actual result': 'NOT EXECUTED', 'Environment / date': 'NOT EXECUTED'}))
        self.assertNotEqual(self.run_generator().returncode, 0)

    def test_stale_check_does_not_write(self):
        target = self.repo / 'test-cases/test-cases.md'
        target.write_text('stale', encoding='utf-8')
        self.assertNotEqual(self.run_generator('--check').returncode, 0)
        self.assertEqual(target.read_text(encoding='utf-8'), 'stale')


if __name__ == '__main__':
    unittest.main()
