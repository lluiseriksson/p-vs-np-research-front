#!/usr/bin/env python3
"""Read-only structural and claim-metadata audit.

This script deliberately does not certify mathematical correctness.
"""

from __future__ import annotations

import json
import hashlib
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

ALLOWED_LABELS = {
    "EXPLORATORY",
    "NUMERICAL",
    "CONDITIONAL",
    "PROVED",
    "FORMALLY VERIFIED",
    "NO-GO",
}

REQUIRED_PATHS = [
    "README.md",
    "docs/problem-statement.md",
    "docs/vertical-map.md",
    "docs/verification-ledger.md",
    "docs/no-go-ledger.md",
    "docs/source-citations",
    "experiments",
    "proofs",
    "formal",
    "verification",
    "artifacts",
]

MODEL_FIELDS = [
    "computational_model",
    "uniformity",
    "circuit_size",
    "circuit_depth",
    "fan_in",
    "randomness",
    "advice",
    "oracle_access",
    "field_or_algebraic_model",
    "asymptotic_quantifiers",
    "case_regime",
]

OPEN_TARGET_IDS = {"T-UNIFORM", "T-NONUNIFORM"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []

    for rel in REQUIRED_PATHS:
        if not (ROOT / rel).exists():
            fail(errors, f"missing required path: {rel}")

    claims_path = ROOT / "verification" / "claims.json"
    try:
        payload = json.loads(claims_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        fail(errors, f"cannot load claims registry: {exc}")
        payload = {"claims": []}

    claims = payload.get("claims")
    if not isinstance(claims, list) or not claims:
        fail(errors, "claims registry must contain a nonempty claims list")
        claims = []

    seen: set[str] = set()
    claim_labels: dict[str, str] = {}
    for index, claim in enumerate(claims):
        prefix = f"claim[{index}]"
        if not isinstance(claim, dict):
            fail(errors, f"{prefix} is not an object")
            continue
        claim_id = claim.get("id")
        if not isinstance(claim_id, str) or not claim_id.strip():
            fail(errors, f"{prefix} has no id")
            claim_id = prefix
        elif claim_id in seen:
            fail(errors, f"duplicate claim id: {claim_id}")
        else:
            seen.add(claim_id)

        label = claim.get("label")
        if label not in ALLOWED_LABELS:
            fail(errors, f"{claim_id}: invalid label {label!r}")
        else:
            claim_labels[claim_id] = label
        if claim_id in OPEN_TARGET_IDS and label != "EXPLORATORY":
            fail(errors, f"{claim_id}: open terminal target must remain EXPLORATORY absent a full-solution audit")
        if not isinstance(claim.get("statement"), str) or not claim["statement"].strip():
            fail(errors, f"{claim_id}: missing statement")
        for field in MODEL_FIELDS:
            value = claim.get(field)
            if not isinstance(value, str) or not value.strip():
                fail(errors, f"{claim_id}: missing model field {field}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for phrase in (
        "Infrastructure maturity",
        "Formally closed proof chain",
        "Real progress toward P vs NP",
    ):
        if phrase not in readme:
            fail(errors, f"README missing progress estimate: {phrase}")

    source_dir = ROOT / "docs" / "source-citations"
    if source_dir.exists():
        source_notes = [p for p in source_dir.glob("*.md") if p.name != "README.md"]
        if len(source_notes) < 8:
            fail(errors, "fewer than eight primary-source notes")

    markdown_link = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
    for markdown in ROOT.rglob("*.md"):
        if ".git" in markdown.parts:
            continue
        text = markdown.read_text(encoding="utf-8")
        for raw_target in markdown_link.findall(text):
            target = raw_target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            resolved = (markdown.parent / target).resolve()
            if not resolved.exists():
                fail(errors, f"broken local link in {markdown.relative_to(ROOT)}: {raw_target}")

    manifest_path = ROOT / "artifacts" / "manifest.json"
    if manifest_path.exists():
        try:
            manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
            entries = manifest.get("files", [])
            if not isinstance(entries, list) or not entries:
                fail(errors, "artifact manifest has no file entries")
            for entry in entries:
                rel = entry.get("path", "")
                expected = entry.get("sha256", "")
                target = ROOT / rel
                if not target.is_file():
                    fail(errors, f"manifest target missing: {rel}")
                    continue
                actual = hashlib.sha256(target.read_bytes()).hexdigest()
                if actual != expected:
                    fail(errors, f"manifest hash mismatch: {rel}")
        except (OSError, json.JSONDecodeError, AttributeError) as exc:
            fail(errors, f"cannot validate artifact manifest: {exc}")

    verification_ledger = (ROOT / "docs/verification-ledger.md").read_text(encoding="utf-8")
    ledger_labels: dict[str, str] = {}
    for line in verification_ledger.splitlines():
        if not line.startswith("|") or line.startswith("|---"):
            continue
        cells = [cell.strip() for cell in line.strip("|").split("|")]
        if len(cells) >= 2 and cells[0] != "ID" and cells[1] not in ALLOWED_LABELS:
            fail(errors, f"verification ledger row has invalid label: {cells[1]}")
        elif len(cells) >= 2 and cells[0] != "ID":
            ledger_labels[cells[0]] = cells[1]

    for claim_id, ledger_label in ledger_labels.items():
        claim_label = claim_labels.get(claim_id)
        if claim_label is not None and claim_label != ledger_label:
            fail(errors, f"label mismatch for {claim_id}: claims={claim_label}, ledger={ledger_label}")

    no_go_ledger = (ROOT / "docs/no-go-ledger.md").read_text(encoding="utf-8")
    explicit_labels = re.findall(r"\*\*Label:\s*([A-Z-]+)\*\*", no_go_ledger)
    for label in explicit_labels:
        if label not in ALLOWED_LABELS:
            fail(errors, f"no-go ledger contains invalid label: {label}")

    for proof in (ROOT / "proofs").glob("*.md"):
        proof_text = proof.read_text(encoding="utf-8")
        match = re.search(r"\*\*Label:\s*([A-Z-]+)", proof_text)
        if match is None:
            fail(errors, f"proof record missing explicit label: {proof.relative_to(ROOT)}")
        elif match.group(1) not in ALLOWED_LABELS:
            fail(errors, f"proof record has invalid label: {proof.relative_to(ROOT)}: {match.group(1)}")

    if errors:
        print("AUDIT FAILED")
        for error in errors:
            print(f"- {error}")
        return 1

    counts = {label: 0 for label in sorted(ALLOWED_LABELS)}
    for claim in claims:
        counts[claim["label"]] += 1
    print("AUDIT PASSED")
    print(f"claims: {len(claims)}")
    for label, count in counts.items():
        print(f"{label}: {count}")
    print("mathematical certification: NOT PERFORMED")
    return 0


if __name__ == "__main__":
    sys.exit(main())
