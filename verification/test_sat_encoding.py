from __future__ import annotations

import unittest

from sat_encoding import (
    context_wrap,
    context_prefix,
    contradiction,
    decode_gamma,
    double_not_wrap,
    encode_and,
    encode_gamma,
    encode_not,
    encode_or,
    encode_variable,
    parse_formula,
    neutral_prefix_family,
    tautology,
    verify_assignment,
)


class GammaEncodingTests(unittest.TestCase):
    def test_round_trip(self) -> None:
        for value in range(1, 500):
            encoded = encode_gamma(value)
            self.assertEqual(decode_gamma(encoded, 0), (value, len(encoded)))

    def test_truncation_rejected(self) -> None:
        self.assertIsNone(decode_gamma("0001", 0))


class FormulaEncodingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.x = encode_variable(1)
        self.y = encode_variable(7)

    def test_parse_and_evaluate(self) -> None:
        formula = encode_and(self.x, encode_not(self.y))
        parsed = parse_formula(formula)
        self.assertIsNotNone(parsed)
        self.assertTrue(verify_assignment(formula, {1: True, 7: False}))
        self.assertFalse(verify_assignment(formula, {1: True, 7: True}))

    def test_or(self) -> None:
        formula = encode_or(self.x, self.y)
        self.assertTrue(verify_assignment(formula, {1: False, 7: True}))

    def test_malformed_and_trailing_bits_rejected(self) -> None:
        self.assertIsNone(parse_formula(""))
        self.assertIsNone(parse_formula("01" + self.x))
        self.assertIsNone(parse_formula(self.x + "0"))
        self.assertIsNone(parse_formula("00"))

    def test_deep_nesting_is_iterative(self) -> None:
        formula = "11" * 5000 + self.x
        parsed = parse_formula(formula)
        self.assertIsNotNone(parsed)
        self.assertTrue(verify_assignment(formula, {1: True}))

    def test_double_not_projection_valid_and_invalid(self) -> None:
        samples = [self.x, encode_and(self.x, self.y), "", "01" + self.x]
        for bits in samples:
            wrapped = double_not_wrap(bits, 3)
            self.assertEqual(parse_formula(bits) is None, parse_formula(wrapped) is None)
            if parse_formula(bits) is not None:
                assignment = {1: True, 7: False}
                self.assertEqual(
                    verify_assignment(bits, assignment),
                    verify_assignment(wrapped, assignment),
                )

    def test_fixed_truth_formulas(self) -> None:
        for value in (False, True):
            self.assertTrue(verify_assignment(tautology(), {1: value}))
            self.assertFalse(verify_assignment(contradiction(), {1: value}))

    def test_context_projection_span_and_semantics(self) -> None:
        samples = [
            self.x,
            encode_and(self.x, self.y),
            "",
            "01" + self.x,
            self.x + "11",
        ]
        l_count, d_count = 2, 4
        start = 12 * l_count + 4 * d_count
        added = start
        for bits in samples:
            wrapped = context_wrap(
                bits,
                left_tautologies=l_count,
                double_nots=d_count,
            )
            self.assertEqual(len(wrapped), len(bits) + added)
            self.assertEqual(wrapped[start : start + len(bits)], bits)
            self.assertEqual(parse_formula(bits) is None, parse_formula(wrapped) is None)
            if parse_formula(bits) is not None:
                for assignment in ({1: False, 7: False}, {1: True, 7: True}):
                    self.assertEqual(
                        verify_assignment(bits, assignment),
                        verify_assignment(wrapped, assignment),
                    )

    def test_right_context_can_repair_malformed_trailing_token(self) -> None:
        malformed = self.x + "11"
        repaired = encode_and(malformed, tautology())
        self.assertIsNone(parse_formula(malformed))
        self.assertIsNotNone(parse_formula(repaired))
        for value in (False, True):
            self.assertFalse(verify_assignment(repaired, {1: value}))

    def test_context_counts_must_be_nonnegative(self) -> None:
        with self.assertRaises(ValueError):
            context_wrap(self.x, left_tautologies=-1)

    def test_neutral_prefix_family(self) -> None:
        k = 5
        prefixes = neutral_prefix_family(k)
        self.assertEqual(len(prefixes), k + 1)
        self.assertEqual(len(set(prefixes)), k + 1)
        for index, prefix in enumerate(prefixes):
            self.assertEqual(len(prefix), 12 * k)
            self.assertEqual(
                prefix,
                context_prefix(
                    left_tautologies=index,
                    double_nots=3 * (k - index),
                ),
            )
            wrapped = prefix + self.y
            self.assertTrue(verify_assignment(wrapped, {1: False, 7: True}))
            self.assertFalse(verify_assignment(wrapped, {1: True, 7: False}))

        for left in range(k + 1):
            for right in range(k + 1):
                distance = sum(
                    a != b for a, b in zip(prefixes[left], prefixes[right])
                )
                self.assertEqual(distance, 6 * abs(left - right))

    def test_neutral_prefix_family_rejects_negative_index(self) -> None:
        with self.assertRaises(ValueError):
            neutral_prefix_family(-1)


if __name__ == "__main__":
    unittest.main()
