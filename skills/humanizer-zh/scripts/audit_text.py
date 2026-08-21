"""Audit Chinese text for template markers and protected-value drift."""

from __future__ import annotations

import argparse
from collections import Counter
import json
from pathlib import Path
import re
import statistics
import sys


SCHEMA_VERSION = "1.0"

MARKER_CATALOG = (
    {"category": "engagement", "confidence": "high", "phrase": "你问到了问题的核心"},
    {"category": "framing", "confidence": "medium", "phrase": "先说结论"},
    {"category": "transition", "confidence": "medium", "phrase": "此外"},
)

PROTECTED_CATEGORIES = (
    "numbers",
    "dates",
    "urls",
    "emails",
    "windows_paths",
    "code_identifiers",
    "quoted_text",
)

COMMON_FILE_EXTENSIONS = frozenset(
    {
        "7z",
        "cfg",
        "com",
        "csv",
        "dll",
        "doc",
        "docx",
        "exe",
        "gif",
        "htm",
        "html",
        "ini",
        "jpeg",
        "jpg",
        "json",
        "log",
        "md",
        "msi",
        "pdf",
        "png",
        "ppt",
        "pptx",
        "py",
        "rar",
        "svg",
        "toml",
        "ts",
        "tsx",
        "txt",
        "webp",
        "xls",
        "xlsx",
        "xml",
        "yaml",
        "yml",
        "zip",
    }
)
PATH_END_OR_CLOSER_CHARS = frozenset("。！？.!?；;)]}")

DATE_RE = re.compile(
    r"(?<![0-9])(?:"
    r"[0-9]{4}年[0-9]{1,2}月[0-9]{1,2}日|"
    r"[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}|"
    r"[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}|"
    r"[0-9]{1,2}月[0-9]{1,2}日"
    r")(?![0-9])"
)
NUMBER_RE = re.compile(
    r"(?<![A-Za-z0-9_.])[+-]?[0-9]+(?:,[0-9]{3})*(?:\.[0-9]+)?%?"
    r"(?![A-Za-z0-9_.])"
)
URL_RE = re.compile(r"https?://[^\s<>\"'“”‘’「」『』，。！？；]+", re.IGNORECASE)
EMAIL_RE = re.compile(
    r"(?<![A-Za-z0-9.!#$%&'*+/=?^_`{|}~-])"
    r"[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+"
    r"(?:\.[A-Za-z0-9!#$%&'*+/=?^_`{|}~-]+)*@"
    r"[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?"
    r"(?:\.[A-Za-z0-9](?:[A-Za-z0-9-]{0,61}[A-Za-z0-9])?)+"
    r"(?![A-Za-z0-9-])"
)
BARE_WINDOWS_PATH_RE = re.compile(
    r"(?<![A-Za-z0-9])[A-Za-z]:\\[^\s<>:\"|?*，。！？；、“”‘’「」『』]*"
)
QUOTED_WINDOWS_PATH_RE = re.compile(r"[A-Za-z]:\\[^\r\n<>:\"|?*]+")
CODE_RE = re.compile(r"`([^`\r\n]+)`")
QUOTE_RES = (
    re.compile(r"“([^”\r\n]+)”"),
    re.compile(r"‘([^’\r\n]+)’"),
    re.compile(r"「([^」\r\n]+)」"),
    re.compile(r"『([^』\r\n]+)』"),
    re.compile(r'(?<!")"([^"\r\n]+)"(?!")'),
    re.compile(r"(?<![A-Za-z0-9'])'([^'\r\n]+)'(?![A-Za-z0-9'])"),
)
SENTENCE_DELIMITER_RE = re.compile(r"[。！？!?；;]+")
PARAGRAPH_DELIMITER_RE = re.compile(r"(?:\r?\n[ \t]*){2,}")


def find_marker_hits(text: str) -> list[dict[str, object]]:
    """Return deterministic non-overlapping counts for known marker phrases."""
    literal_matches = [*CODE_RE.finditer(text), *_quote_matches(text)]
    marker_text = _mask_spans(
        text,
        [(match.start(), match.end()) for match in literal_matches],
    )
    hits = []
    for marker in MARKER_CATALOG:
        count = marker_text.count(marker["phrase"])
        if count:
            hits.append({**marker, "count": count})
    return sorted(
        hits,
        key=lambda hit: (hit["confidence"], hit["category"], hit["phrase"]),
    )


def analyze_structure(text: str) -> dict[str, int | float]:
    """Measure visible content, paragraphs, and non-empty sentence lengths."""
    characters = sum(not character.isspace() for character in text)
    stripped = text.strip()
    paragraphs = (
        sum(bool(paragraph.strip()) for paragraph in PARAGRAPH_DELIMITER_RE.split(stripped))
        if stripped
        else 0
    )
    sentence_lengths = [
        sum(not character.isspace() for character in sentence)
        for sentence in SENTENCE_DELIMITER_RE.split(text)
    ]
    sentence_lengths = [length for length in sentence_lengths if length]

    if sentence_lengths:
        average = round(statistics.fmean(sentence_lengths), 2)
        stddev = round(statistics.pstdev(sentence_lengths), 2)
    else:
        average = 0.0
        stddev = 0.0

    return {
        "characters": characters,
        "paragraphs": paragraphs,
        "sentences": len(sentence_lengths),
        "average_sentence_length": average,
        "sentence_length_stddev": stddev,
    }


def _strip_ascii_tail_and_unpaired_closers(value: str) -> str:
    pairs = {")": "(", "]": "[", "}": "{"}
    opener_counts = Counter(character for character in value if character in pairs.values())
    closer_counts = Counter(character for character in value if character in pairs)
    end = len(value)

    while end:
        while end and value[end - 1] in ";,.!?":
            end -= 1
        if not end or value[end - 1] not in pairs:
            break
        closer = value[end - 1]
        if closer_counts[closer] <= opener_counts[pairs[closer]]:
            break
        closer_counts[closer] -= 1
        end -= 1

    return value[:end]


def _quote_matches(text: str) -> list[re.Match[str]]:
    matches = []
    for pattern in QUOTE_RES:
        matches.extend(
            match for match in pattern.finditer(text) if match.group(1).strip()
        )
    return sorted(matches, key=lambda match: (match.start(), match.end()))


def _mask_spans(text: str, spans: list[tuple[int, int]]) -> str:
    characters = list(text)
    for start, end in spans:
        characters[start:end] = " " * (end - start)
    return "".join(characters)


def _bare_path_has_explicit_terminator(
    text: str, match: re.Match[str], value: str
) -> bool:
    following = text[match.end() :]
    if not following:
        return True
    if following[0] in "\r\n":
        return True

    raw_value = match.group(0)
    stripped_tail = raw_value[len(value) :]
    if stripped_tail and stripped_tail[0] in PATH_END_OR_CLOSER_CHARS:
        return True

    if value.endswith("\\"):
        return True

    last_segment = value.rsplit("\\", 1)[-1]
    _, separator, extension = last_segment.rpartition(".")
    if separator and extension.casefold() in COMMON_FILE_EXTENSIONS:
        return True

    remainder = following.lstrip()
    return bool(remainder and remainder[0] in PATH_END_OR_CLOSER_CHARS)


def extract_protected(text: str) -> dict[str, list[str]]:
    """Extract protected values in fixed categories with deterministic ordering."""
    date_matches = list(DATE_RE.finditer(text))
    dates = [match.group(0) for match in date_matches]

    url_matches = list(URL_RE.finditer(text))
    urls = []
    for match in url_matches:
        value = _strip_ascii_tail_and_unpaired_closers(match.group(0))
        if value:
            urls.append(value)

    email_matches = list(EMAIL_RE.finditer(text))
    emails = [match.group(0) for match in email_matches]
    code_matches = list(CODE_RE.finditer(text))
    quote_matches = _quote_matches(text)
    code_identifiers = [match.group(1) for match in code_matches]
    quoted_text = [match.group(1) for match in quote_matches]

    protected_spans = [(match.start(), match.end()) for match in code_matches]
    protected_spans.extend((match.start(), match.end()) for match in quote_matches)
    bare_path_text = _mask_spans(text, protected_spans)

    windows_paths = []
    bare_path_spans = []
    for match in BARE_WINDOWS_PATH_RE.finditer(bare_path_text):
        value = _strip_ascii_tail_and_unpaired_closers(match.group(0))
        if len(value) >= 3 and _bare_path_has_explicit_terminator(
            bare_path_text, match, value
        ):
            windows_paths.append(value)
            bare_path_spans.append((match.start(), match.end()))

    enclosed_values = [match.group(1) for match in code_matches]
    enclosed_values.extend(match.group(1) for match in quote_matches)
    for value in enclosed_values:
        if QUOTED_WINDOWS_PATH_RE.fullmatch(value):
            windows_paths.append(value)

    number_spans = [
        *((match.start(), match.end()) for match in date_matches),
        *((match.start(), match.end()) for match in url_matches),
        *((match.start(), match.end()) for match in email_matches),
        *((match.start(), match.end()) for match in code_matches),
        *((match.start(), match.end()) for match in quote_matches),
        *bare_path_spans,
    ]
    number_text = _mask_spans(text, number_spans)
    numbers = [match.group(0) for match in NUMBER_RE.finditer(number_text)]

    extracted = {
        "numbers": numbers,
        "dates": dates,
        "urls": urls,
        "emails": emails,
        "windows_paths": windows_paths,
        "code_identifiers": code_identifiers,
        "quoted_text": quoted_text,
    }
    return {category: sorted(extracted[category]) for category in PROTECTED_CATEGORIES}


def compare_protected(source: str, candidate: str) -> dict[str, dict[str, list[str]]]:
    """Compare protected values as multisets, preserving the category schema."""
    source_values = extract_protected(source)
    candidate_values = extract_protected(candidate)
    changes = {}
    for category in PROTECTED_CATEGORIES:
        source_counter = Counter(source_values[category])
        candidate_counter = Counter(candidate_values[category])
        changes[category] = {
            "added": sorted((candidate_counter - source_counter).elements()),
            "removed": sorted((source_counter - candidate_counter).elements()),
        }
    return changes


def build_report(candidate: str, source: str | None = None) -> dict[str, object]:
    """Build the versioned audit report."""
    marker_hits = find_marker_hits(candidate)
    high_count = sum(
        int(hit["count"]) for hit in marker_hits if hit["confidence"] == "high"
    )
    medium_count = sum(
        int(hit["count"]) for hit in marker_hits if hit["confidence"] == "medium"
    )
    marker_summary = {
        "high": high_count,
        "medium": medium_count,
        "total": high_count + medium_count,
    }

    comparison_performed = source is not None
    protected_changes = compare_protected(source, candidate) if source is not None else None

    warnings = []
    if high_count:
        warnings.append(f"发现 {high_count} 处高置信模板化信号，请人工复核。")
    if medium_count:
        warnings.append(f"发现 {medium_count} 处中置信模板化信号，请结合文体复核。")
    if protected_changes is not None:
        changed_categories = [
            category
            for category in PROTECTED_CATEGORIES
            if protected_changes[category]["added"]
            or protected_changes[category]["removed"]
        ]
        if changed_categories:
            warnings.append(
                "受保护信息发生变化："
                + "、".join(changed_categories)
                + "，请核对改写是否保真。"
            )

    return {
        "schema_version": SCHEMA_VERSION,
        "comparison_performed": comparison_performed,
        "marker_summary": marker_summary,
        "marker_hits": marker_hits,
        "structure": analyze_structure(candidate),
        "protected_changes": protected_changes,
        "warnings": warnings,
    }


def _format_human_report(report: dict[str, object]) -> str:
    summary = report["marker_summary"]
    structure = report["structure"]
    lines = [
        (
            "模板化信号："
            f"high={summary['high']}，medium={summary['medium']}，total={summary['total']}"
        ),
        (
            "结构："
            f"characters={structure['characters']}，paragraphs={structure['paragraphs']}，"
            f"sentences={structure['sentences']}"
        ),
    ]

    changes = report["protected_changes"]
    if changes is None:
        lines.append("受保护信息：未进行来源比较")
    else:
        changed_categories = [
            category
            for category in PROTECTED_CATEGORIES
            if changes[category]["added"] or changes[category]["removed"]
        ]
        if changed_categories:
            lines.append("受保护信息变化：")
            for category in changed_categories:
                added = changes[category]["added"]
                removed = changes[category]["removed"]
                lines.append(
                    f"{category}: removed={', '.join(removed) or '-'}; "
                    f"added={', '.join(added) or '-'}"
                )
        else:
            lines.append("无受保护信息变化")

    warnings = report["warnings"]
    if warnings:
        lines.append("警告：")
        lines.extend(warnings)
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="审计文本中的模板化信号和保真信息。")
    parser.add_argument("--candidate", required=True, help="待审计文本文件")
    parser.add_argument("--source", help="可选的来源文本文件")
    parser.add_argument("--json", action="store_true", help="输出 JSON 报告")
    try:
        args = parser.parse_args(argv)
    except SystemExit as exc:
        return int(exc.code)

    try:
        candidate = Path(args.candidate).read_text(encoding="utf-8-sig")
        source = (
            Path(args.source).read_text(encoding="utf-8-sig")
            if args.source is not None
            else None
        )
    except (OSError, UnicodeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2

    report = build_report(candidate, source=source)
    if args.json:
        print(json.dumps(report, ensure_ascii=False))
    else:
        print(_format_human_report(report))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
