from __future__ import annotations

import itertools
import unittest

from sat_encoding import (
    assignment_conjunction,
    annihilating_prefix,
    context_wrap,
    conditioned_prefix,
    context_prefix,
    contradiction,
    decode_gamma,
    double_not_wrap,
    encode_and,
    encode_gamma,
    encode_not,
    encode_or,
    encode_variable,
    evaluate,
    parse_formula,
    neutral_prefix_family,
    neutral_prefix_index,
    operator_square_prefix,
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

    @staticmethod
    def brute_sat(bits: str, forced: dict[int, bool] | None = None) -> bool:
        parsed = parse_formula(bits)
        if parsed is None:
            return False
        assignment = dict(forced or {})
        free = sorted(parsed.variables - assignment.keys())
        for values in itertools.product((False, True), repeat=len(free)):
            trial = assignment | dict(zip(free, values))
            if evaluate(parsed, trial):
                return True
        return False

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

    def test_neutral_prefix_regular_recognizer(self) -> None:
        for k in range(8):
            prefixes = neutral_prefix_family(k)
            for index, prefix in enumerate(prefixes):
                self.assertEqual(neutral_prefix_index(prefix), index)
                if prefix:
                    flipped = ("1" if prefix[0] == "0" else "0") + prefix[1:]
                    self.assertIsNone(neutral_prefix_index(flipped))
        self.assertIsNone(neutral_prefix_index("1"))
        self.assertIsNone(neutral_prefix_index("x" * 12))

    def test_annihilating_prefix(self) -> None:
        prefix = annihilating_prefix()
        neutral = context_prefix(left_tautologies=1)
        self.assertEqual(len(prefix), 12)
        self.assertEqual(sum(a != b for a, b in zip(prefix, neutral)), 2)
        samples = [self.x, self.y, encode_or(self.x, self.y), "", self.x + "11"]
        for bits in samples:
            wrapped = prefix + bits
            self.assertFalse(verify_assignment(wrapped, {1: True, 7: True}))
            self.assertEqual(parse_formula(bits) is None, parse_formula(wrapped) is None)

    def test_operator_square_is_one_hot_on_nonempty_suffixes(self) -> None:
        suffixes = [self.x, self.y, encode_or(self.x, self.y), self.x + "11"]
        for token in ("00", "01", "10", "11"):
            prefix = operator_square_prefix(token)
            self.assertEqual(len(prefix), 12)
            for suffix in suffixes:
                wrapped = prefix + suffix
                expected = token == "10" and verify_assignment(
                    suffix, {1: True, 7: True}
                )
                self.assertEqual(
                    verify_assignment(wrapped, {1: True, 7: True}), expected
                )
        self.assertEqual(operator_square_prefix("10"), context_prefix(left_tautologies=1))
        self.assertEqual(operator_square_prefix("01"), annihilating_prefix())
        with self.assertRaises(ValueError):
            operator_square_prefix("xx")

    def test_equal_length_conditioned_sat_prefixes(self) -> None:
        prefixes = {value: conditioned_prefix(value) for value in (False, True)}
        self.assertEqual({len(prefix) for prefix in prefixes.values()}, {14})
        suffixes = [
            self.x,
            encode_not(self.x),
            self.y,
            encode_or(self.x, encode_not(self.x)),
            encode_and(self.x, encode_not(self.x)),
            self.x + "11",
        ]
        for suffix in suffixes:
            branches = []
            for value in (False, True):
                branch = self.brute_sat(prefixes[value] + suffix)
                expected = self.brute_sat(suffix, {1: value})
                self.assertEqual(branch, expected)
                branches.append(branch)
            self.assertEqual(any(branches), self.brute_sat(suffix))

    def test_conditioned_prefix_length_by_identifier_bit_length(self) -> None:
        for bit_length in range(1, 7):
            identifiers = range(2 ** (bit_length - 1), 2**bit_length)
            lengths = {
                len(conditioned_prefix(value, identifier))
                for identifier in identifiers
                for value in (False, True)
            }
            self.assertEqual(lengths, {4 * bit_length + 10})

    def test_assignment_witnesses_shatter_conditioned_outputs(self) -> None:
        identifiers = tuple(range(4, 8))
        expected_length = len(identifiers) * (4 * 3 + 10) - 2
        observed_vectors: set[tuple[bool, ...]] = set()
        for values in itertools.product((False, True), repeat=len(identifiers)):
            assignment = dict(zip(identifiers, values))
            formula = assignment_conjunction(assignment)
            self.assertEqual(len(formula), expected_length)
            parsed = parse_formula(formula)
            self.assertIsNotNone(parsed)
            self.assertEqual(parsed.variables, frozenset(identifiers))

            output_vector = []
            for identifier in identifiers:
                for forced_value in (False, True):
                    output = self.brute_sat(
                        conditioned_prefix(forced_value, identifier) + formula
                    )
                    self.assertEqual(output, forced_value == assignment[identifier])
                    output_vector.append(output)
            observed_vectors.add(tuple(output_vector))

            padded = double_not_wrap(formula, 3)
            self.assertEqual(len(padded), expected_length + 12)
            for identifier in identifiers:
                for forced_value in (False, True):
                    self.assertEqual(
                        self.brute_sat(
                            conditioned_prefix(forced_value, identifier) + padded
                        ),
                        forced_value == assignment[identifier],
                    )

        self.assertEqual(len(observed_vectors), 2 ** len(identifiers))

    def test_assignment_conjunction_rejects_empty_map(self) -> None:
        with self.assertRaises(ValueError):
            assignment_conjunction({})


if __name__ == "__main__":
    unittest.main()
