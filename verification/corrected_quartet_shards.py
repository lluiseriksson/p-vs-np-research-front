"""Fail-closed shards for the corrected GATE-004AD quartet domain."""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
from typing import Iterable

from quartet_type_audit import LENGTH68_REPAIR_IDENTIFIERS
from quartet_type_audit_fast import QuartetAuditor


SCHEMA_VERSION = 1
FIRST_FAILURE_LIMIT = 10


@dataclass(frozen=True)
class AuditConfig:
    bound: int
    gap_cap: int
    representative_length: int
    max_blocks: int
    identifiers: tuple[int, ...]


PRODUCTION_CONFIG = AuditConfig(
    bound=68,
    gap_cap=139,
    representative_length=600,
    max_blocks=3,
    identifiers=LENGTH68_REPAIR_IDENTIFIERS,
)


def _alphabet_sha256(identifiers: tuple[int, ...]) -> str:
    payload = ",".join(map(str, identifiers)).encode("ascii")
    return sha256(payload).hexdigest()


def _engine_sha256() -> str:
    return sha256(Path(__file__).read_bytes()).hexdigest()


def _result_sha256(result: dict[str, object]) -> str:
    payload = dict(result)
    payload.pop("result_sha256", None)
    encoded = json.dumps(
        payload, sort_keys=True, separators=(",", ":")
    ).encode("utf-8")
    return sha256(encoded).hexdigest()


def run_shard(
    residue: int,
    gap_1_start: int,
    gap_1_end: int,
    *,
    config: AuditConfig = PRODUCTION_CONFIG,
) -> dict[str, object]:
    """Audit one half-open first-gap shard and return a sealed JSON object."""
    if residue not in range(4):
        raise ValueError("residue must be 0, 1, 2, or 3")
    if not 1 <= gap_1_start < gap_1_end <= config.gap_cap + 1:
        raise ValueError("invalid half-open first-gap interval")
    minimum_length = (
        config.bound + 3 + 3 * config.gap_cap + config.bound
    )
    if config.representative_length <= minimum_length:
        raise ValueError("representative length lacks a strict right margin")

    auditor = QuartetAuditor(config.identifiers, config.representative_length)
    first = config.bound + residue
    failures: list[tuple[tuple[int, ...], tuple[int, ...]]] = []
    failure_count = 0
    checked = 0
    for gap_1 in range(gap_1_start, gap_1_end):
        for gap_2 in range(1, config.gap_cap + 1):
            for gap_3 in range(1, config.gap_cap + 1):
                quartet = (
                    first,
                    first + gap_1,
                    first + gap_1 + gap_2,
                    first + gap_1 + gap_2 + gap_3,
                )
                reached = auditor.reached_masks_positions(
                    quartet, config.max_blocks
                )
                missing = tuple(
                    mask
                    for mask in range(1, 15)
                    if not (reached >> mask) & 1
                )
                if missing:
                    failure_count += 1
                    if len(failures) < FIRST_FAILURE_LIMIT:
                        failures.append((quartet, missing))
                checked += 1

    result: dict[str, object] = {
        "schema_version": SCHEMA_VERSION,
        "complete": True,
        "engine": "QuartetAuditor.reached_masks_positions",
        "config": {
            "bound": config.bound,
            "gap_cap": config.gap_cap,
            "representative_length": config.representative_length,
            "max_blocks": config.max_blocks,
            "identifier_count": len(config.identifiers),
            "alphabet_sha256": _alphabet_sha256(config.identifiers),
            "engine_sha256": _engine_sha256(),
        },
        "residue": residue,
        "gap_1_start": gap_1_start,
        "gap_1_end": gap_1_end,
        "checked": checked,
        "failure_count": failure_count,
        "first_failures": failures,
    }
    result["result_sha256"] = _result_sha256(result)
    return result


def merge_shards(
    shards: Iterable[dict[str, object]],
    *,
    config: AuditConfig = PRODUCTION_CONFIG,
) -> dict[str, object]:
    """Validate exact domain coverage and merge sealed shard summaries."""
    expected_config = {
        "bound": config.bound,
        "gap_cap": config.gap_cap,
        "representative_length": config.representative_length,
        "max_blocks": config.max_blocks,
        "identifier_count": len(config.identifiers),
        "alphabet_sha256": _alphabet_sha256(config.identifiers),
        "engine_sha256": _engine_sha256(),
    }
    by_residue: dict[int, list[tuple[int, int]]] = {r: [] for r in range(4)}
    total_checked = 0
    total_failures = 0
    first_failures = []
    shard_count = 0
    counterexample_auditor: QuartetAuditor | None = None
    for shard in shards:
        shard_count += 1
        if shard.get("schema_version") != SCHEMA_VERSION:
            raise ValueError("shard schema mismatch")
        if shard.get("complete") is not True:
            raise ValueError("incomplete shard")
        if shard.get("config") != expected_config:
            raise ValueError("shard configuration mismatch")
        if shard.get("result_sha256") != _result_sha256(shard):
            raise ValueError("shard seal mismatch")
        residue = shard.get("residue")
        start = shard.get("gap_1_start")
        end = shard.get("gap_1_end")
        if (
            not isinstance(residue, int)
            or residue not in range(4)
            or not isinstance(start, int)
            or not isinstance(end, int)
            or not 1 <= start < end <= config.gap_cap + 1
        ):
            raise ValueError("invalid shard interval")
        expected_checked = (end - start) * config.gap_cap**2
        if shard.get("checked") != expected_checked:
            raise ValueError("shard checked-count mismatch")
        failure_count = shard.get("failure_count")
        failures = shard.get("first_failures")
        if (
            not isinstance(failure_count, int)
            or failure_count < 0
            or not isinstance(failures, list)
            or len(failures) > min(FIRST_FAILURE_LIMIT, failure_count)
            or (failure_count > 0 and not failures)
        ):
            raise ValueError("invalid shard failure summary")
        for failure in failures:
            if (
                not isinstance(failure, (list, tuple))
                or len(failure) != 2
                or not isinstance(failure[0], (list, tuple))
                or len(failure[0]) != 4
                or not all(isinstance(value, int) for value in failure[0])
                or not isinstance(failure[1], (list, tuple))
                or not failure[1]
                or not all(
                    isinstance(mask, int) and 1 <= mask <= 14
                    for mask in failure[1]
                )
            ):
                raise ValueError("malformed first counterexample")
            quartet = tuple(failure[0])
            missing = tuple(failure[1])
            gaps = tuple(
                quartet[index + 1] - quartet[index] for index in range(3)
            )
            if (
                quartet[0] != config.bound + residue
                or not start <= gaps[0] < end
                or any(not 1 <= gap <= config.gap_cap for gap in gaps)
            ):
                raise ValueError("counterexample lies outside its shard")
            if counterexample_auditor is None:
                counterexample_auditor = QuartetAuditor(
                    config.identifiers, config.representative_length
                )
            reached = counterexample_auditor.reached_masks_positions(
                quartet, config.max_blocks
            )
            actual_missing = tuple(
                mask for mask in range(1, 15) if not (reached >> mask) & 1
            )
            if missing != actual_missing:
                raise ValueError("counterexample does not reproduce")
        by_residue[residue].append((start, end))
        total_checked += expected_checked
        total_failures += failure_count
        for failure in failures:
            if len(first_failures) < FIRST_FAILURE_LIMIT:
                first_failures.append(failure)

    for residue, intervals in by_residue.items():
        cursor = 1
        for start, end in sorted(intervals):
            if start != cursor:
                kind = "overlap" if start < cursor else "gap"
                raise ValueError(f"residue {residue} has shard {kind}")
            cursor = end
        if cursor != config.gap_cap + 1:
            raise ValueError(f"residue {residue} has incomplete coverage")

    expected_total = 4 * config.gap_cap**3
    if total_checked != expected_total:
        raise ValueError("merged checked count does not equal full domain")
    return {
        "schema_version": SCHEMA_VERSION,
        "complete": True,
        "config": expected_config,
        "shard_count": shard_count,
        "checked": total_checked,
        "failure_count": total_failures,
        "first_failures": first_failures,
        "universality_certificate": total_failures == 0,
    }


def _load_json(path: Path) -> dict[str, object]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"{path} does not contain a JSON object")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    commands = parser.add_subparsers(dest="command", required=True)
    run = commands.add_parser("run")
    run.add_argument("residue", type=int)
    run.add_argument("gap_1_start", type=int)
    run.add_argument("gap_1_end", type=int)
    merge = commands.add_parser("merge")
    merge.add_argument("shards", nargs="+", type=Path)
    arguments = parser.parse_args()
    if arguments.command == "run":
        result = run_shard(
            arguments.residue, arguments.gap_1_start, arguments.gap_1_end
        )
    else:
        result = merge_shards(_load_json(path) for path in arguments.shards)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
