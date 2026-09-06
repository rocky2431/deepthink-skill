"""Check the portable plugin surface; native loading and behavior are separate."""

import json
import re
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    plugin = root / "plugins" / "deep-thinking"
    skill = plugin / "skills" / "deep-thinking"
    manifest_paths = [
        plugin / ".codex-plugin" / "plugin.json",
        plugin / ".claude-plugin" / "plugin.json",
        plugin / ".zcode-plugin" / "plugin.json",
        plugin / "kimi.plugin.json",
    ]
    manifests = [json.loads(path.read_text()) for path in manifest_paths]
    version = manifests[0]["version"]
    assert re.fullmatch(r"\d+\.\d+\.\d+(?:\+[0-9A-Za-z.-]+)?", version), version
    assert "+codex." not in version, "Local cachebuster must not become the public release version"
    for path, manifest in zip(manifest_paths, manifests):
        assert manifest["name"] == plugin.name, path
        assert manifest["version"] == version, path
        assert not {"hooks", "commands", "mcpServers", "apps"} & manifest.keys(), path
    assert manifests[0]["skills"] == "./skills/"
    assert manifests[2]["skills"] == "skills"
    assert manifests[3]["skills"] == ["./skills"]
    assert list(plugin.rglob("SKILL.md")) == [skill / "SKILL.md"]
    entry = (skill / "SKILL.md").read_text()
    assert re.search(r"(?m)^name: deep-thinking$", entry)

    codex_catalog = json.loads((root / ".agents/plugins/marketplace.json").read_text())
    claude_catalog = json.loads((root / ".claude-plugin/marketplace.json").read_text())
    assert codex_catalog["name"] == claude_catalog["name"] == "rocky-deep-thinking"
    for catalog in (codex_catalog, claude_catalog):
        assert [item["name"] for item in catalog["plugins"]] == [plugin.name]
    assert codex_catalog["plugins"][0]["source"]["path"] == "./plugins/deep-thinking"
    assert claude_catalog["plugins"][0]["source"] == "./plugins/deep-thinking"
    assert "version" not in claude_catalog["metadata"]
    assert "version" not in claude_catalog["plugins"][0]

    links = 0
    for path in [*plugin.rglob("*"), *root.glob("*.md")]:
        assert not path.is_symlink(), path
        if not path.is_file():
            continue
        assert path.suffix in {".md", ".json", ".yaml"}, path
        body = path.read_text()
        assert body.endswith("\n"), path
        assert all(line == line.rstrip() for line in body.splitlines()), path
        assert "/Users/" not in body and "/var/folders/" not in body, path
        if path.suffix != ".md":
            continue
        for target in re.findall(r"\]\(([^)]+)\)", body):
            if re.match(r"[a-zA-Z][a-zA-Z0-9+.-]*:", target):
                continue
            relative = target.split("#", 1)[0]
            if not relative:
                continue
            destination = (path.parent / relative).resolve()
            boundary = plugin if path.is_relative_to(plugin) else root
            assert destination.is_relative_to(boundary.resolve()), (path, target)
            assert destination.exists(), (path, target)
            links += 1
    assert (skill / "assets/thoughts-template.md").is_file()
    assert (skill / "assets/result-template.md").is_file()
    assert (skill / "agents/openai.yaml").is_file()
    print(f"PASS: four manifests at {version}, one Skill, catalogs, {links} local links, portable package.")


if __name__ == "__main__":
    main()
