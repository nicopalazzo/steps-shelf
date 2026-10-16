#!/usr/bin/env python3
"""Cheap checks that need no login: manifests parse, the version is semver and in the changelog,
the licence matches LICENSE, the marketplace points at this folder, and the skill and page exist."""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
errors = []


def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as e:
        errors.append(f"{path.relative_to(ROOT)}: cannot read as JSON ({e})")
        return {}


licence = (ROOT / "LICENSE").read_text(encoding="utf-8")
expected = "MIT" if licence.startswith("MIT License") else None
if expected is None:
    errors.append("LICENSE: does not start with 'MIT License' (update this check if the licence changes)")

manifest = load(ROOT / ".claude-plugin" / "plugin.json")
market = load(ROOT / ".claude-plugin" / "marketplace.json")

name = manifest.get("name")
version = str(manifest.get("version", ""))
if name != "steps-shelf":
    errors.append(f"plugin.json: name is {name!r}")
if not SEMVER.match(version):
    errors.append(f"plugin.json: version {version!r} is not semver")
if expected and manifest.get("license") != expected:
    errors.append(f"plugin.json: licence is {manifest.get('license')!r}, LICENSE says {expected}")
if "author" not in manifest:
    errors.append("plugin.json: no author")

listed = {p.get("name"): p for p in market.get("plugins", [])}
if name not in listed:
    errors.append("marketplace.json: steps-shelf is not listed")
elif listed[name].get("source") != "./":
    errors.append(f"marketplace.json: source is {listed[name].get('source')!r}, expected './'")

changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
if f"## [{version}]" not in changelog:
    errors.append(f"CHANGELOG.md: no entry for {version}")

skill = ROOT / "skills" / "steps-shelf" / "SKILL.md"
text = skill.read_text(encoding="utf-8") if skill.exists() else ""
front = text.split("---")[1] if text.count("---") >= 2 else ""
if "name:" not in front or "description:" not in front:
    errors.append("skills/steps-shelf/SKILL.md: front matter needs name and description")

page = ROOT / "page" / "shelf.html"
if not page.exists() or "<title>" not in page.read_text(encoding="utf-8"):
    errors.append("page/shelf.html: missing or has no <title>")

LINK = "claude.ai/" + "artifact/"
SKIP_DIRS = {".git", "docs"}
for path in ROOT.rglob("*"):
    if not path.is_file() or SKIP_DIRS & set(path.relative_to(ROOT).parts):
        continue
    try:
        body = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        continue
    if LINK in body:
        errors.append(f"{path.relative_to(ROOT)}: contains a shelf link; keep it in ~/.claude/steps-shelf-url")

if errors:
    print("\n".join(errors))
    sys.exit(1)
print(f"ok: steps-shelf {version}, licence {expected}")
