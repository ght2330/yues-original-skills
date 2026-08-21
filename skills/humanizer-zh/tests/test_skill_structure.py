from __future__ import annotations

import hashlib
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]
SKILL_PATH = ROOT / "SKILL.md"
REFERENCES = ROOT / "references"

REFERENCE_HEADINGS = {
    "zh-patterns.md": (
        "## 高置信信号",
        "## 中置信信号",
        "## 篇章级模式",
        "## 局部模式",
        "## 保护上下文",
    ),
    "genre-profiles.md": (
        "## general",
        "## public-account",
        "## xiaohongshu",
        "## spoken-script",
        "## technical",
        "## academic",
    ),
    "voice-matching.md": (
        "## 可匹配的形式信号",
        "## 不可迁移的语义内容",
        "## 启用与降级",
    ),
    "evaluation.md": (
        "## 首轮自动验收",
        "## 安全金标",
        "## 后续内容评估",
    ),
}

PRESERVED_HASHES = {
    ".gitignore": "E52AAC198ACD71945E1730F45CAFBA41FFFDA4E2A0D7D6A38175880AAE8EABEA",
    "LICENSE": "AA00E74769E1B9D8E7FA7094DBFCCA9B129A0DED6DCE1CF4DA050B99146D2FA7",
    "README.md": "60CD3ED8B4753837CA8F8FCEBF6076A38591A269D91EA1791AA7448E5A1B1B58",
}


class SkillStructureTests(unittest.TestCase):
    def test_frontmatter_has_only_name_and_description(self):
        text = SKILL_PATH.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---", text, re.DOTALL)

        self.assertIsNotNone(match)
        keys = re.findall(r"^([A-Za-z0-9_-]+):", match.group(1), re.MULTILINE)
        self.assertEqual(["name", "description"], keys)

    def test_router_is_small_and_links_every_reference(self):
        text = SKILL_PATH.read_text(encoding="utf-8")

        self.assertLessEqual(len(text.splitlines()), 240)
        for filename in REFERENCE_HEADINGS:
            self.assertIn(f"references/{filename}", text)

    def test_references_have_exact_required_headings(self):
        for filename, headings in REFERENCE_HEADINGS.items():
            lines = (REFERENCES / filename).read_text(encoding="utf-8").splitlines()
            for heading in headings:
                self.assertIn(heading, lines, f"{filename} missing {heading}")

    def test_runtime_markdown_has_no_old_fabricated_example(self):
        paths = [SKILL_PATH, *(REFERENCES / name for name in REFERENCE_HEADINGS)]
        runtime_text = "\n".join(path.read_text(encoding="utf-8") for path in paths)

        for phrase in (
            "批处理、键盘快捷键和离线模式",
            "来自测试用户的早期反馈",
            "添加了具体功能和具体反馈",
        ):
            self.assertNotIn(phrase, runtime_text)

    def test_openai_metadata_is_exact_and_neutral(self):
        text = (ROOT / "agents" / "openai.yaml").read_text(encoding="utf-8")
        self.assertEqual(
            [
                "interface:",
                '  display_name: "Humanizer 中文文本自然化"',
                '  short_description: "诊断并保真改写中文文本，减少模板腔并保留事实、语气和作者声音"',
                '  default_prompt: "Use $humanizer-zh to edit this Chinese text in the mode and genre appropriate to my request, preserving facts and existing voice."',
            ],
            text.strip().splitlines(),
        )

    def test_preserved_files_match_pre_change_hashes(self):
        for filename, expected in PRESERVED_HASHES.items():
            actual = hashlib.sha256((ROOT / filename).read_bytes()).hexdigest().upper()
            self.assertEqual(expected, actual, filename)

    def test_safety_gold_has_one_complete_passing_batch(self):
        text = (REFERENCES / "evaluation.md").read_text(encoding="utf-8")
        rows = [line for line in text.splitlines() if re.match(r"^\| G\d{2} ", line)]

        self.assertEqual(12, len(rows))
        self.assertTrue(all("| PASS，" in row for row in rows))
        case_ids = [re.match(r"^\| (G\d{2}) ", row).group(1) for row in rows]
        self.assertEqual([f"G{index:02d}" for index in range(1, 13)], case_ids)

        row_batch_ids = [re.findall(r"FT-\d{8}-v\d+", row) for row in rows]
        self.assertTrue(all(len(batch_ids) == 1 for batch_ids in row_batch_ids))
        self.assertEqual(
            {"FT-20260717-v4"},
            {batch_ids[0] for batch_ids in row_batch_ids},
        )


if __name__ == "__main__":
    unittest.main()
