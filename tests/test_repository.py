"""Portable package contracts, independent of design-quality evaluation."""
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/web-motion-director"


def anchors(text):
    result, counts = set(), {}
    fence = None
    for line in text.splitlines():
        token = re.match(r"\s*(`{3,}|~{3,})", line)
        if token:
            mark = token.group(1)
            if fence is None:
                fence = mark
            elif mark[0] == fence[0] and len(mark) >= len(fence):
                fence = None
            continue
        if fence:
            continue
        heading = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if heading:
            slug = re.sub(r"[^\w\s-]", "", heading.group(1).lower()).replace(" ", "-")
            count = counts.get(slug, 0)
            result.add(slug + (f"-{count}" if count else ""))
            counts[slug] = count + 1
    return result


class PackageTests(unittest.TestCase):
    def test_core_is_compact_and_has_standard_frontmatter(self):
        text = (SKILL / "SKILL.md").read_text()
        self.assertTrue(text.startswith("---\nname: web-motion-director\ndescription: "))
        self.assertEqual(len(text.split("---", 2)[1].strip().splitlines()), 2)
        self.assertLess(len(text.splitlines()), 500)

    def test_manifest_and_core_version_agree(self):
        version = json.loads((ROOT / "plugin.json").read_text())["version"]
        self.assertIn(f"Package version: {version}.", (SKILL / "SKILL.md").read_text())

    def test_local_links_and_fragments_resolve(self):
        for source in ROOT.rglob("*.md"):
            if ".git" in source.parts:
                continue
            for target in re.findall(r"\]\(([^\s)]+)", source.read_text()):
                if re.match(r"^[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                    continue
                path, _, fragment = target.partition("#")
                destination = (source.parent / path).resolve() if path else source
                self.assertTrue(destination.is_relative_to(ROOT), (source, target))
                self.assertTrue(destination.exists(), (source, target))
                if fragment and destination.suffix == ".md":
                    self.assertIn(fragment, anchors(destination.read_text()), (source, target))

    def test_authored_instructions_are_portable(self):
        for source in [*SKILL.rglob("*.md"), SKILL / "agents/openai.yaml"]:
            text = source.read_text()
            self.assertNotIn("/workspace/scratch/", text, source)
            self.assertNotIn("/root/.codex/", text, source)
            self.assertNotIn(chr(0x2014), text, source)

    def test_both_original_mit_notices_remain(self):
        for path in (ROOT / "LICENSE", SKILL / "LICENSE"):
            text = path.read_text()
            self.assertIn("MIT License", text)
            self.assertIn("Permission is hereby granted", text)
            self.assertIn("Copyright", text)


if __name__ == "__main__":
    unittest.main()
