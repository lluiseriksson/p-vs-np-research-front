from __future__ import annotations

import unittest

from sat_encoding import (
    decode_gamma,
    double_not_wrap,
    encode_and,
    encode_gamma,
    encode_not,
    encode_or,
    encode_variable,
    parse_formula,
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


if __name__ == "__main__":
    unittest.main()
