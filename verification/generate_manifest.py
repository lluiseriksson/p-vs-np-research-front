#!/usr/bin/env python3
"""Regenerate the deterministic SHA-256 source manifest."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "artifacts" / "manifest.json"
EXCLUDED_PARTS = {".git", ".pytest_cache", "__pycache__"}


def included(path: Path) -> bool:
    rel = path.relative_to(ROOT)
    if any(part in EXCLUDED_PARTS for part in rel.parts):
        return False
    return path != OUTPUT and not path.name.endswith(".pyc")


def main() -> None:
    entries = []
    for path in sorted(p for p in ROOT.rglob("*") if p.is_file() and included(p)):
        rel = path.relative_to(ROOT).as_posix()
        entries.append(
            {
                "path": rel,
                "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            }
        )
    payload = {
        "schema_version": 1,
        "generator": "python verification/generate_manifest.py",
        "files": entries,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)} with {len(entries)} entries")


if __name__ == "__main__":
    main()
