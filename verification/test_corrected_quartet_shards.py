"""Fail-closed contract tests for corrected quartet shards."""

from __future__ import annotations

from copy import deepcopy
import unittest

from corrected_quartet_shards import (
    AuditConfig,
    merge_shards,
    run_shard,
)
from quartet_type_audit import LENGTH68_REPAIR_IDENTIFIERS


TINY = AuditConfig(
    bound=68,
    gap_cap=3,
    representative_length=160,
    max_blocks=3,
    identifiers=LENGTH68_REPAIR_IDENTIFIERS,
)


class CorrectedQuartetShardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.shards = [
            run_shard(residue, 1, 4, config=TINY)
            for residue in range(4)
        ]

    def test_complete_tiny_domain_merges(self) -> None:
        merged = merge_shards(self.shards, config=TINY)
        self.assertEqual(merged["checked"], 4 * 3**3)
        self.assertEqual(merged["failure_count"], 0)
        self.assertTrue(merged["universality_certificate"])

    def test_missing_residue_fails_closed(self) -> None:
        with self.assertRaisesRegex(ValueError, "incomplete coverage"):
            merge_shards(self.shards[:-1], config=TINY)

    def test_overlap_fails_closed(self) -> None:
        split = []
        for residue in range(4):
            split.append(run_shard(residue, 1, 3, config=TINY))
            split.append(run_shard(residue, 2, 4, config=TINY))
        with self.assertRaisesRegex(ValueError, "overlap"):
            merge_shards(split, config=TINY)

    def test_tampered_count_fails_closed(self) -> None:
        tampered = deepcopy(self.shards)
        tampered[0]["checked"] = 0
        with self.assertRaisesRegex(ValueError, "seal mismatch"):
            merge_shards(tampered, config=TINY)

    def test_different_engine_hash_fails_closed(self) -> None:
        tampered = deepcopy(self.shards)
        tampered[0]["config"]["engine_sha256"] = "0" * 64
        with self.assertRaisesRegex(ValueError, "configuration mismatch"):
            merge_shards(tampered, config=TINY)


if __name__ == "__main__":
    unittest.main()
