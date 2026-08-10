"""Regression certificates for large-gap quartet component budgets."""

from __future__ import annotations

import unittest

from triple_component_audit import (
    full_zero_triple_failures,
    single_zero_pair_failures,
)


class TripleComponentAuditTests(unittest.TestCase):
    def test_every_pair_singleton_zero_uses_one_block(self) -> None:
        self.assertEqual(single_zero_pair_failures(), ())

    def test_every_triple_full_zero_uses_three_blocks(self) -> None:
        self.assertEqual(full_zero_triple_failures(), ())


if __name__ == "__main__":
    unittest.main()
