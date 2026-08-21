import importlib.util
import json
from pathlib import Path
import re
import subprocess
import sys
import tempfile
import time
import unittest


SKILL_DIR = Path(__file__).resolve().parents[1]
SCRIPT_PATH = SKILL_DIR / "scripts" / "audit_text.py"
FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"
PROTECTED_KEYS = [
    "numbers",
    "dates",
    "urls",
    "emails",
    "windows_paths",
    "code_identifiers",
    "quoted_text",
]
FORBIDDEN_CLAIM_PATTERNS = (
    re.compile(
        r"(?:AI|人工智能).{0,24}(?:概率|生成|撰写|作者身份|probability|generated?|written|authorship)",
        re.IGNORECASE | re.DOTALL,
    ),
    re.compile(
        r"(?:概率|生成|撰写|作者身份|probability|generated?|written|authorship).{0,24}(?:AI|人工智能)",
        re.IGNORECASE | re.DOTALL,
    ),
)
CLAIM_SEGMENT_RE = re.compile(r"[。！？!?；;，,\r\n]+|(?=但(?:是)?|然而|不过)")
SAFE_NEGATION_SCOPE_RE = re.compile(
    r"(?:不判断|不提供|不会输出|无法判断|不用于判断)[^。！？!?；;，,]{0,24}$"
)


def find_forbidden_claims(output):
    matches = []
    for segment in CLAIM_SEGMENT_RE.split(output):
        if not segment:
            continue
        for pattern in FORBIDDEN_CLAIM_PATTERNS:
            for match in pattern.finditer(segment):
                if SAFE_NEGATION_SCOPE_RE.search(segment[: match.start()]):
                    continue
                matches.append(match.group(0))
    return matches


def load_audit_module():
    spec = importlib.util.spec_from_file_location("humanizer_zh_audit_text", SCRIPT_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"无法从 {SCRIPT_PATH} 创建模块规格")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def setUpModule():
    global audit_text
    audit_text = load_audit_module()


class MarkerTests(unittest.TestCase):
    def test_marker_counts_and_hit_sorting_are_deterministic(self):
        text = "你问到了问题的核心。你问到了问题的核心。此外，先说结论。"

        report = audit_text.build_report(text)
        hits = report["marker_hits"]

        self.assertEqual(
            {"high": 2, "medium": 2, "total": 4},
            report["marker_summary"],
        )
        self.assertEqual(
            3,
            len(hits),
        )
        phrases = [hit["phrase"] for hit in hits]
        self.assertEqual(len(phrases), len(set(phrases)))
        self.assertEqual(
            [
                ("你问到了问题的核心", 2),
                ("先说结论", 1),
                ("此外", 1),
            ],
            sorted((hit["phrase"], hit["count"]) for hit in hits),
        )
        sort_keys = [
            (hit["confidence"], hit["category"], hit["phrase"])
            for hit in hits
        ]
        self.assertEqual(sorted(sort_keys), sort_keys)

    def test_find_marker_hits_exposes_required_fields(self):
        hits = audit_text.find_marker_hits("此外。")

        self.assertEqual(1, len(hits))
        self.assertLessEqual(
            {"confidence", "category", "phrase", "count"},
            hits[0].keys(),
        )
        self.assertEqual("medium", hits[0]["confidence"])
        self.assertEqual("此外", hits[0]["phrase"])
        self.assertEqual(1, hits[0]["count"])

    def test_markers_inside_quotes_and_code_are_not_counted(self):
        hits = audit_text.find_marker_hits(
            "正文此外。引文写着“此外”，代码是 `先说结论`。"
        )

        self.assertEqual(
            [("此外", 1)],
            [(hit["phrase"], hit["count"]) for hit in hits],
        )


class StructureTests(unittest.TestCase):
    def test_structure_uses_content_length_and_population_stddev(self):
        structure = audit_text.analyze_structure("甲乙。丙丁丁！\n\n第四段；")

        self.assertEqual(11, structure["characters"])
        self.assertEqual(2, structure["paragraphs"])
        self.assertEqual(3, structure["sentences"])
        self.assertEqual(2.67, structure["average_sentence_length"])
        self.assertEqual(0.47, structure["sentence_length_stddev"])

    def test_empty_text_has_zero_average_and_stddev(self):
        structure = audit_text.analyze_structure("")

        self.assertEqual(0.0, structure["average_sentence_length"])
        self.assertEqual(0.0, structure["sentence_length_stddev"])

    def test_chinese_and_ascii_sentence_delimiters_are_supported(self):
        structure = audit_text.analyze_structure("甲。乙！丙？丁!戊?己；庚;")

        self.assertEqual(7, structure["sentences"])


class ProtectedExtractionTests(unittest.TestCase):
    def test_protected_comparison_is_ordered_and_uses_multiset_differences(self):
        source = (
            "日期 2025-01-02；数字 42、42、7；"
            "网址 https://old.example/path；邮箱 old@example.com；"
            "路径 C:\\Work\\old.txt；代码 `old_name`；引文“原话”。"
        )
        candidate = (
            "日期 2026-03-04；数字 42、8、8；"
            "网址 https://new.example/path；邮箱 new@example.com；"
            "路径 D:\\Work\\new.txt；代码 `new_name`；引文“新话”。"
        )

        source_values = audit_text.extract_protected(source)
        candidate_values = audit_text.extract_protected(candidate)
        changes = audit_text.compare_protected(source, candidate)

        self.assertEqual(PROTECTED_KEYS, list(source_values))
        self.assertEqual(PROTECTED_KEYS, list(candidate_values))
        self.assertEqual(PROTECTED_KEYS, list(changes))
        self.assertEqual(["42", "42", "7"], source_values["numbers"])
        self.assertEqual(["42", "8", "8"], candidate_values["numbers"])
        self.assertEqual(["2025-01-02"], source_values["dates"])
        self.assertEqual(["https://old.example/path"], source_values["urls"])
        self.assertEqual(["old@example.com"], source_values["emails"])
        self.assertEqual([r"C:\Work\old.txt"], source_values["windows_paths"])
        self.assertEqual(["old_name"], source_values["code_identifiers"])
        self.assertEqual(["原话"], source_values["quoted_text"])
        self.assertEqual({"added": ["8", "8"], "removed": ["42", "7"]}, changes["numbers"])
        self.assertEqual(
            {"added": ["2026-03-04"], "removed": ["2025-01-02"]},
            changes["dates"],
        )
        self.assertEqual(
            {"added": ["https://new.example/path"], "removed": ["https://old.example/path"]},
            changes["urls"],
        )
        self.assertEqual(
            {"added": ["new@example.com"], "removed": ["old@example.com"]},
            changes["emails"],
        )
        self.assertEqual(
            {"added": [r"D:\Work\new.txt"], "removed": [r"C:\Work\old.txt"]},
            changes["windows_paths"],
        )
        self.assertEqual(
            {"added": ["new_name"], "removed": ["old_name"]},
            changes["code_identifiers"],
        )
        self.assertEqual(
            {"added": ["新话"], "removed": ["原话"]},
            changes["quoted_text"],
        )
        for category in PROTECTED_KEYS:
            self.assertEqual(sorted(source_values[category]), source_values[category])
            self.assertEqual(sorted(candidate_values[category]), candidate_values[category])
            self.assertEqual(sorted(changes[category]["added"]), changes[category]["added"])
            self.assertEqual(sorted(changes[category]["removed"]), changes[category]["removed"])

    def test_numbers_are_found_next_to_chinese_text(self):
        values = audit_text.extract_protected("共3人，增长20%，第2章。")

        self.assertEqual(["2", "20%", "3"], values["numbers"])

    def test_numbers_inside_other_protected_values_are_not_duplicated(self):
        values = audit_text.extract_protected(
            "日期 2026-07-17；网址 https://example.test/1；"
            "邮箱 1@example.com；路径 C:\\2026\\report.txt；"
            "代码 `42`；引文“7”；普通数字 9。"
        )

        self.assertEqual(["9"], values["numbers"])

    def test_url_stops_before_chinese_sentence_punctuation(self):
        values = audit_text.extract_protected("https://a.test。然后继续")

        self.assertEqual(["https://a.test"], values["urls"])

    def test_email_stops_before_adjacent_chinese_text(self):
        values = audit_text.extract_protected("邮箱a@example.com联系")

        self.assertEqual(["a@example.com"], values["emails"])

    def test_apostrophes_in_contractions_are_not_quotes(self):
        values = audit_text.extract_protected("don't can't 'quoted text'")

        self.assertEqual(["quoted text"], values["quoted_text"])

    def test_empty_quoted_values_are_not_protected(self):
        values = audit_text.extract_protected(
            "“” ‘’ 「」 『』 \"\" '' “   ” '   '"
        )

        self.assertEqual([], values["quoted_text"])

    def test_windows_path_strips_trailing_parenthesis_and_period(self):
        values = audit_text.extract_protected(r"(C:\Work\a.txt).")

        self.assertEqual([r"C:\Work\a.txt"], values["windows_paths"])

    def test_windows_path_with_spaces_is_found_inside_quotes(self):
        values = audit_text.extract_protected("“C:\\Program Files\\App\\a.txt”")

        self.assertEqual([r"C:\Program Files\App\a.txt"], values["windows_paths"])

    def test_url_with_many_unpaired_closers_is_cleaned_in_linear_time(self):
        text = "https://example.test/path" + ")" * 60_000

        started = time.perf_counter()
        values = audit_text.extract_protected(text)
        elapsed = time.perf_counter() - started

        self.assertEqual(["https://example.test/path"], values["urls"])
        self.assertLess(
            elapsed,
            1.0,
            msg=f"清理 60,000 个尾闭括号耗时 {elapsed:.3f}s，应保持线性复杂度",
        )

    def test_windows_root_path_is_protected(self):
        values = audit_text.extract_protected(r"根目录 C:\。")

        self.assertEqual(["C:\\"], values["windows_paths"])

    def test_unquoted_windows_path_with_spaces_is_not_partially_reported(self):
        values = audit_text.extract_protected(r"路径 C:\Program Files\App\a.txt。")

        self.assertEqual([], values["windows_paths"])

    def test_unquoted_program_files_path_without_later_slash_is_not_partial(self):
        values = audit_text.extract_protected(r"C:\Program Files。")

        self.assertEqual([], values["windows_paths"])

    def test_unquoted_my_documents_path_is_not_partial(self):
        values = audit_text.extract_protected(r"C:\My Documents。")

        self.assertEqual([], values["windows_paths"])

    def test_ambiguous_prose_after_bare_path_is_not_treated_as_a_terminator(self):
        values = audit_text.extract_protected(r"C:\Temp then slash \ character.")

        self.assertEqual([], values["windows_paths"])

    def test_line_break_ends_a_bare_path(self):
        for line_break in ("\n", "\r\n"):
            with self.subTest(line_break=repr(line_break)):
                values = audit_text.extract_protected(
                    "C:\\Temp" + line_break + "Next line"
                )

                self.assertEqual([r"C:\Temp"], values["windows_paths"])

    def test_ascii_period_ends_a_bare_path_before_next_sentence(self):
        values = audit_text.extract_protected(r"C:\Temp. Next sentence")

        self.assertEqual([r"C:\Temp"], values["windows_paths"])

    def test_ascii_period_ends_a_bare_path_before_line_break(self):
        values = audit_text.extract_protected("C:\\Temp.\nNext")

        self.assertEqual([r"C:\Temp"], values["windows_paths"])

    def test_unquoted_documents_and_settings_is_not_partially_reported(self):
        values = audit_text.extract_protected(r"C:\Documents and Settings.")

        self.assertEqual([], values["windows_paths"])

    def test_two_bare_paths_separated_by_a_connector_are_both_protected(self):
        values = audit_text.extract_protected(r"C:\one.txt and D:\two.txt")

        self.assertEqual(
            [r"C:\one.txt", r"D:\two.txt"],
            values["windows_paths"],
        )


class ReportTests(unittest.TestCase):
    def test_warning_order_and_text_are_stable(self):
        source = "原数字是 1。"
        candidate = "你问到了问题的核心。此外，数字是 2。"

        report = audit_text.build_report(candidate, source=source)

        self.assertEqual(
            [
                "发现 1 处高置信模板化信号，请人工复核。",
                "发现 1 处中置信模板化信号，请结合文体复核。",
                "受保护信息发生变化：numbers，请核对改写是否保真。",
            ],
            report["warnings"],
        )

    def test_report_without_source_skips_comparison(self):
        report = audit_text.build_report("此外。")

        self.assertFalse(report["comparison_performed"])
        self.assertIsNone(report["protected_changes"])


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(SCRIPT_PATH), *map(str, args)],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="strict",
            check=False,
            timeout=5,
        )

    def assert_only_stderr_error(self, result):
        self.assertEqual(2, result.returncode)
        self.assertEqual("", result.stdout)
        self.assertNotEqual("", result.stderr)

    def assert_no_forbidden_claims(self, output):
        self.assertEqual([], find_forbidden_claims(output))

    def test_forbidden_claim_patterns_cover_variants_without_overmatching(self):
        forbidden = (
            "AI 生成概率为 80%",
            "该文本由 AI 撰写",
            "人工智能生成内容",
        )
        for claim in forbidden:
            with self.subTest(claim=claim):
                self.assertTrue(find_forbidden_claims(claim))
        safe_statements = (
            "本工具不判断作者身份",
            "本工具不判断 AI 生成概率，也不判断作者身份。",
            "本报告不会输出 AI 生成概率。",
        )
        for statement in safe_statements:
            with self.subTest(statement=statement):
                self.assert_no_forbidden_claims(statement)
        self.assertTrue(
            find_forbidden_claims(
                "本工具不判断 AI 生成概率，但该文本由 AI 撰写。"
            )
        )

    def test_json_cli_accepts_utf8_bom_and_emits_versioned_report(self):
        with tempfile.TemporaryDirectory() as directory:
            directory = Path(directory)
            source_path = directory / "source.txt"
            candidate_path = directory / "candidate.txt"
            source_path.write_text("原值是 1。", encoding="utf-8-sig")
            candidate_path.write_text("此外，新值是 2。", encoding="utf-8-sig")

            result = self.run_cli(
                "--candidate",
                candidate_path,
                "--source",
                source_path,
                "--json",
            )

        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stderr)
        report = json.loads(result.stdout)
        self.assertEqual("1.0", report["schema_version"])
        self.assertTrue(report["comparison_performed"])
        self.assertEqual(1, report["marker_summary"]["medium"])
        self.assertEqual(
            ["2"],
            report["protected_changes"]["numbers"]["added"],
        )
        self.assertEqual(
            ["1"],
            report["protected_changes"]["numbers"]["removed"],
        )
        self.assertIn(
            "发现 1 处中置信模板化信号，请结合文体复核。",
            report["warnings"],
        )
        self.assertIn(
            "受保护信息发生变化：numbers，请核对改写是否保真。",
            report["warnings"],
        )
        self.assert_no_forbidden_claims(result.stdout)

    def test_missing_candidate_file_returns_2_on_stderr(self):
        with tempfile.TemporaryDirectory() as directory:
            missing = Path(directory) / "missing.txt"
            result = self.run_cli("--candidate", missing, "--json")

        self.assert_only_stderr_error(result)

    def test_invalid_utf8_returns_2_on_stderr(self):
        with tempfile.TemporaryDirectory() as directory:
            candidate_path = Path(directory) / "invalid.txt"
            candidate_path.write_bytes(b"\xff\xfe\x00")
            result = self.run_cli("--candidate", candidate_path, "--json")

        self.assert_only_stderr_error(result)

    def test_missing_candidate_argument_returns_2_with_usage_on_stderr(self):
        result = self.run_cli("--json")

        self.assert_only_stderr_error(result)
        self.assertIn("usage:", result.stderr.lower())

    def test_non_json_report_is_human_readable_and_avoids_authorship_claims(self):
        result = self.run_cli(
            "--candidate",
            FIXTURES_DIR / "candidate.txt",
            "--source",
            FIXTURES_DIR / "source.txt",
        )

        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stderr)
        self.assertIn("模板化信号", result.stdout)
        number_change_lines = [
            line for line in result.stdout.splitlines() if "numbers" in line
        ]
        self.assertTrue(
            any(
                re.search(r"(?<!\d)1(?!\d)", line)
                and re.search(r"(?<!\d)2(?!\d)", line)
                for line in number_change_lines
            ),
            msg="非 JSON 报告应同行展示 numbers 从 1 变为 2",
        )
        self.assertIn(
            "发现 1 处中置信模板化信号，请结合文体复核。",
            result.stdout,
        )
        self.assertIn(
            "受保护信息发生变化：numbers，请核对改写是否保真。",
            result.stdout,
        )
        self.assert_no_forbidden_claims(result.stdout)

    def test_non_json_report_explicitly_says_protected_values_are_unchanged(self):
        source_path = FIXTURES_DIR / "source.txt"

        result = self.run_cli(
            "--candidate",
            source_path,
            "--source",
            source_path,
        )

        self.assertEqual(0, result.returncode)
        self.assertEqual("", result.stderr)
        self.assertIn("无受保护信息变化", result.stdout)


if __name__ == "__main__":
    unittest.main()
