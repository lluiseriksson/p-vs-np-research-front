from __future__ import annotations

import itertools
import unittest

from sat_encoding import (
    assignment_conjunction,
    annihilating_prefix,
    context_wrap,
    conditioned_prefix,
    common_outer_double_not_pad,
    coordinate_dense_distant_pairs,
    coordinate_dense_neutral_paddings,
    context_prefix,
    contradiction,
    decode_gamma,
    distant_outer_triples,
    double_not_wrap,
    encode_and,
    encode_gamma,
    encode_not,
    encode_or,
    encode_variable,
    evaluate,
    pair_zero_neutral_padding,
    parse_formula,
    satisfiability_padding_wrap,
    neutral_prefix_family,
    neutral_prefix_index,
    one_two_block_neutral_paddings,
    one_bit_auxiliary_identifier,
    one_bit_conditioned_prefix,
    one_bit_context_cube_prefix,
    one_bit_halo_prefixes,
    one_bit_literal_gadgets,
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

    def test_one_bit_exact_literal_gadgets(self) -> None:
        identifiers = (1, 3, 6, 7, 12, 13, 14, 15, 24, 31)
        for identifier in identifiers:
            binary = format(identifier, "b")
            auxiliary = (
                3
                if identifier == 1
                else int("1" + binary[2:] + "11", 2)
            )
            gadgets = one_bit_literal_gadgets(identifier)
            self.assertEqual(len(gadgets[False]), len(gadgets[True]))
            self.assertEqual(
                sum(a != b for a, b in zip(gadgets[False], gadgets[True])),
                1,
            )
            bit_length = identifier.bit_length()
            self.assertEqual(len(gadgets[True]), 6 * bit_length + 11)
            self.assertEqual(
                len(one_bit_conditioned_prefix(True, identifier)),
                6 * bit_length + 13,
            )
            for target_value in (False, True):
                for auxiliary_value in (False, True):
                    assignment = {
                        identifier: target_value,
                        auxiliary: auxiliary_value,
                    }
                    self.assertEqual(
                        verify_assignment(gadgets[True], assignment), target_value
                    )
                    self.assertEqual(
                        verify_assignment(gadgets[False], assignment), not target_value
                    )

            auxiliary_variable = encode_variable(auxiliary)
            target_variable = encode_variable(identifier)
            suffixes = (
                auxiliary_variable,
                encode_not(auxiliary_variable),
                encode_or(target_variable, auxiliary_variable),
                encode_and(target_variable, encode_not(auxiliary_variable)),
            )
            prefixes = {
                value: one_bit_conditioned_prefix(value, identifier)
                for value in (False, True)
            }
            self.assertEqual(
                sum(a != b for a, b in zip(prefixes[False], prefixes[True])),
                1,
            )
            for suffix in suffixes:
                branches = []
                for value in (False, True):
                    branch = self.brute_sat(prefixes[value] + suffix)
                    self.assertEqual(
                        branch,
                        self.brute_sat(suffix, {identifier: value}),
                    )
                    branches.append(branch)
                self.assertEqual(any(branches), self.brute_sat(suffix))

    def test_one_bit_literal_gadget_rejects_unsupported_identifier(self) -> None:
        for identifier in (0, 2, 4, 5, 8):
            with self.assertRaises(ValueError):
                one_bit_literal_gadgets(identifier)

    def test_adjacent_conditioning_rows_form_affine_parallel_edges(self) -> None:
        def xor(left: str, right: str) -> str:
            self.assertEqual(len(left), len(right))
            return "".join("1" if a != b else "0" for a, b in zip(left, right))

        for bit_length in range(2, 8):
            context_width = bit_length - 2

            def identifier(context: int) -> int:
                suffix = format(context, f"0{context_width}b") if context_width else ""
                return int("11" + suffix, 2)

            base = one_bit_conditioned_prefix(True, identifier(0))
            edge = xor(base, one_bit_conditioned_prefix(False, identifier(0)))
            edge_support = {index for index, bit in enumerate(edge) if bit == "1"}
            self.assertEqual(edge_support, {3 * bit_length + 10})

            directions = []
            occupied = set(edge_support)
            for context_bit in range(context_width):
                unit_context = 1 << (context_width - context_bit - 1)
                direction = xor(
                    base,
                    one_bit_conditioned_prefix(True, identifier(unit_context)),
                )
                support = {index for index, bit in enumerate(direction) if bit == "1"}
                self.assertEqual(len(support), 3)
                self.assertTrue(occupied.isdisjoint(support))
                occupied.update(support)
                directions.append(direction)

            for context in range(2**context_width):
                for polarity in (False, True):
                    reconstructed = list(base)
                    if not polarity:
                        reconstructed = [
                            "1" if bit != delta else "0"
                            for bit, delta in zip(reconstructed, edge)
                        ]
                    for context_bit, direction in enumerate(directions):
                        if context & (1 << (context_width - context_bit - 1)):
                            reconstructed = [
                                "1" if bit != delta else "0"
                                for bit, delta in zip(reconstructed, direction)
                            ]
                    self.assertEqual(
                        "".join(reconstructed),
                        one_bit_conditioned_prefix(polarity, identifier(context)),
                    )

    def test_one_bit_off_cube_halo_has_six_exact_semantics(self) -> None:
        def xor_support(left: str, right: str) -> set[int]:
            self.assertEqual(len(left), len(right))
            return {
                index
                for index, bits in enumerate(zip(left, right))
                if bits[0] != bits[1]
            }

        for bit_length in range(3, 7):
            context_width = bit_length - 2
            for context in range(2**context_width):
                suffix = format(context, f"0{context_width}b")
                identifier = int("11" + suffix, 2)
                for context_bit in range(context_width):
                    toggled_identifier = identifier ^ (
                        1 << (context_width - context_bit - 1)
                    )
                    auxiliary = one_bit_auxiliary_identifier(identifier)
                    toggled_auxiliary = one_bit_auxiliary_identifier(
                        toggled_identifier
                    )
                    variables = sorted(
                        {
                            identifier,
                            toggled_identifier,
                            auxiliary,
                            toggled_auxiliary,
                        }
                    )
                    for polarity in (False, True):
                        base = one_bit_conditioned_prefix(polarity, identifier)
                        opposite_context = one_bit_conditioned_prefix(
                            polarity, toggled_identifier
                        )
                        direction_support = xor_support(base, opposite_context)
                        self.assertEqual(len(direction_support), 3)

                        halo = one_bit_halo_prefixes(
                            polarity, identifier, context_bit
                        )
                        self.assertEqual(set(halo), {"first", "middle", "final"})
                        singleton_supports = []
                        for prefix in halo.values():
                            self.assertEqual(len(prefix), len(base))
                            support = xor_support(base, prefix)
                            self.assertEqual(len(support), 1)
                            singleton_supports.append(support)
                            parsed = parse_formula(prefix[2:])
                            self.assertIsNotNone(parsed)
                        self.assertEqual(
                            set().union(*singleton_supports), direction_support
                        )

                        for values in itertools.product(
                            (False, True), repeat=len(variables)
                        ):
                            assignment = dict(zip(variables, values))
                            x = assignment[identifier]
                            xp = assignment[toggled_identifier]
                            k = assignment[auxiliary]
                            if polarity:
                                expected = {
                                    "first": (xp and not k) or x,
                                    "middle": x,
                                    "final": (x and not k) or xp,
                                }
                            else:
                                expected = {
                                    "first": not x,
                                    "middle": (not x) or (not xp),
                                    "final": not xp,
                                }
                            for position, prefix in halo.items():
                                self.assertEqual(
                                    verify_assignment(prefix[2:], assignment),
                                    expected[position],
                                )

    def test_three_copy_context_cube_has_exact_affine_semantics(self) -> None:
        def xor_support(left: str, right: str) -> set[int]:
            self.assertEqual(len(left), len(right))
            return {
                index
                for index, bits in enumerate(zip(left, right))
                if bits[0] != bits[1]
            }

        for bit_length in range(3, 6):
            context_width = bit_length - 2

            def identifier(context: int) -> int:
                suffix = format(context, f"0{context_width}b")
                return int("11" + suffix, 2)

            contexts = range(2**context_width)
            base_identifier = identifier(0)
            base = one_bit_context_cube_prefix(
                True, base_identifier, base_identifier, base_identifier
            )
            polarity_support = xor_support(
                base,
                one_bit_context_cube_prefix(
                    False, base_identifier, base_identifier, base_identifier
                ),
            )
            self.assertEqual(polarity_support, {3 * bit_length + 10})

            directions: dict[tuple[int, int], str] = {}
            occupied = set(polarity_support)
            for position in range(3):
                for context_bit in range(context_width):
                    unit = 1 << (context_width - context_bit - 1)
                    triple = [base_identifier] * 3
                    triple[position] = identifier(unit)
                    changed = one_bit_context_cube_prefix(True, *triple)
                    support = xor_support(base, changed)
                    self.assertEqual(len(support), 1)
                    self.assertTrue(occupied.isdisjoint(support))
                    occupied.update(support)
                    directions[(position, context_bit)] = changed

            for first_context in contexts:
                for middle_context in contexts:
                    for final_context in contexts:
                        triple = (
                            identifier(first_context),
                            identifier(middle_context),
                            identifier(final_context),
                        )
                        variables = sorted(
                            {
                                triple[0],
                                triple[1],
                                triple[2],
                                one_bit_auxiliary_identifier(triple[1]),
                            }
                        )
                        for polarity in (False, True):
                            prefix = one_bit_context_cube_prefix(
                                polarity, *triple
                            )
                            self.assertEqual(len(prefix), 6 * bit_length + 13)
                            self.assertIsNotNone(parse_formula(prefix[2:]))

                            reconstructed = list(base)
                            if not polarity:
                                for index in polarity_support:
                                    reconstructed[index] = (
                                        "1" if reconstructed[index] == "0" else "0"
                                    )
                            for position, context in enumerate(
                                (first_context, middle_context, final_context)
                            ):
                                for context_bit in range(context_width):
                                    if context & (
                                        1 << (context_width - context_bit - 1)
                                    ):
                                        changed = directions[(position, context_bit)]
                                        for index in xor_support(base, changed):
                                            reconstructed[index] = (
                                                "1"
                                                if reconstructed[index] == "0"
                                                else "0"
                                            )
                            self.assertEqual("".join(reconstructed), prefix)

                            for values in itertools.product(
                                (False, True), repeat=len(variables)
                            ):
                                assignment = dict(zip(variables, values))
                                if polarity:
                                    expected = (
                                        assignment[triple[0]]
                                        and not assignment[
                                            one_bit_auxiliary_identifier(triple[1])
                                        ]
                                    ) or assignment[triple[2]]
                                else:
                                    expected = (
                                        assignment[triple[0]]
                                        and not assignment[triple[1]]
                                    ) or not assignment[triple[2]]
                                self.assertEqual(
                                    verify_assignment(prefix[2:], assignment),
                                    expected,
                                )

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

    def test_assignment_witnesses_pad_to_every_larger_length(self) -> None:
        identifiers = (4, 5, 6)
        assignment = {4: False, 5: True, 6: False}
        formula = assignment_conjunction(assignment)
        for extra_length in range(12, 40):
            padded = satisfiability_padding_wrap(formula, extra_length)
            self.assertEqual(len(padded), len(formula) + extra_length)
            self.assertIsNotNone(parse_formula(padded))
            for identifier in identifiers:
                for forced_value in (False, True):
                    self.assertEqual(
                        self.brute_sat(
                            conditioned_prefix(forced_value, identifier) + padded
                        ),
                        forced_value == assignment[identifier],
                    )

    def test_common_outer_padding_reserves_raw_one_coordinates(self) -> None:
        identifiers = (6, 7, 12)
        formulas = tuple(
            assignment_conjunction(dict(zip(identifiers, values)))
            for values in itertools.product((False, True), repeat=len(identifiers))
        )
        reserved_ones = 20
        total_length = max(map(len, formulas)) + reserved_ones + 40
        for formula in formulas:
            padded = common_outer_double_not_pad(
                formula, total_length, reserved_ones
            )
            self.assertEqual(len(padded), total_length)
            self.assertEqual(padded[:reserved_ones], "1" * reserved_ones)
            self.assertIsNotNone(parse_formula(padded))
            for identifier in identifiers:
                for forced_value in (False, True):
                    self.assertEqual(
                        self.brute_sat(
                            conditioned_prefix(forced_value, identifier) + padded
                        ),
                        self.brute_sat(
                            conditioned_prefix(forced_value, identifier) + formula
                        ),
                    )

    def test_coordinate_dense_neutral_padding_varies_every_outer_bit(self) -> None:
        formulas = (
            encode_variable(1),
            encode_not(encode_variable(2)),
            assignment_conjunction({6: False, 7: True}),
            "",
            "01" + encode_variable(1),
        )
        for extra_length in range(16, 65, 4):
            for formula in formulas:
                padded_family = coordinate_dense_neutral_paddings(
                    formula, extra_length
                )
                self.assertTrue(padded_family)
                for padded in padded_family:
                    self.assertEqual(len(padded), len(formula) + extra_length)
                    self.assertEqual(
                        self.brute_sat(padded), self.brute_sat(formula)
                    )
                    self.assertEqual(
                        parse_formula(padded) is not None,
                        parse_formula(formula) is not None,
                    )
                for position in range(extra_length):
                    self.assertEqual(
                        {padded[position] for padded in padded_family},
                        {"0", "1"},
                    )

    def test_distant_pair_clauses_hold_on_every_dense_context(self) -> None:
        formulas = (
            encode_variable(1),
            assignment_conjunction({6: False, 7: True}),
            "",
        )
        for extra_length in range(32, 129, 4):
            pairs = coordinate_dense_distant_pairs(extra_length)
            self.assertEqual(len(pairs), extra_length // 2)
            self.assertEqual(
                {position for pair in pairs for position in pair},
                set(range(extra_length)),
            )
            for formula in formulas:
                for padded in coordinate_dense_neutral_paddings(
                    formula, extra_length
                ):
                    for left, right in pairs:
                        self.assertNotEqual(
                            (padded[left], padded[right]),
                            ("0", "0"),
                        )

    def test_one_or_two_blocks_zero_every_nonroot_pair(self) -> None:
        unavoidable = {(0, 1), (0, 2), (1, 3), (2, 3)}
        certificate_lengths = tuple(range(32, 88, 4)) + (128,)
        formula = encode_variable(1)
        for extra_length in certificate_lengths:
            missing = set()
            for left in range(extra_length):
                for right in range(left, extra_length):
                    padded = pair_zero_neutral_padding(
                        formula, extra_length, left, right
                    )
                    if padded is None:
                        missing.add((left, right))
                        continue
                    self.assertEqual(len(padded), len(formula) + extra_length)
                    self.assertEqual(padded[left], "0")
                    self.assertEqual(padded[right], "0")
                    self.assertTrue(self.brute_sat(padded))
            self.assertEqual(missing, unavoidable)

        malformed = "01" + formula
        for pair in ((4, 5), (14, 15), (31, 63), (60, 63)):
            padded = pair_zero_neutral_padding(malformed, 64, *pair)
            self.assertIsNotNone(padded)
            self.assertIsNone(parse_formula(padded or ""))

    def test_two_block_contexts_leave_every_distant_triple_clause_true(self) -> None:
        formula = encode_variable(1)
        extra_length = 84
        triples = distant_outer_triples(extra_length)
        contexts = one_two_block_neutral_paddings(formula, extra_length)
        self.assertTrue(contexts)
        for padded in contexts:
            self.assertEqual(len(padded), len(formula) + extra_length)
            for triple in triples:
                self.assertNotEqual(
                    tuple(padded[position] for position in triple),
                    ("0", "0", "0"),
                )
        sample_stride = max(1, len(contexts) // 25)
        for padded in contexts[::sample_stride]:
            self.assertTrue(self.brute_sat(padded))

    def test_satisfiability_padding_rejects_short_increment(self) -> None:
        with self.assertRaises(ValueError):
            satisfiability_padding_wrap(self.x, 11)

    def test_assignment_witnesses_form_affine_subspace(self) -> None:
        identifiers = (4, 5, 6, 7)
        zero_assignment = {identifier: False for identifier in identifiers}
        base = assignment_conjunction(zero_assignment)

        def xor(left: str, right: str) -> str:
            self.assertEqual(len(left), len(right))
            return "".join("1" if a != b else "0" for a, b in zip(left, right))

        directions = {}
        occupied: set[int] = set()
        for identifier in identifiers:
            unit = dict(zero_assignment)
            unit[identifier] = True
            direction = xor(base, assignment_conjunction(unit))
            support = {i for i, bit in enumerate(direction) if bit == "1"}
            self.assertTrue(support)
            self.assertTrue(occupied.isdisjoint(support))
            occupied.update(support)
            directions[identifier] = direction

        for values in itertools.product((False, True), repeat=len(identifiers)):
            assignment = dict(zip(identifiers, values))
            reconstructed = list(base)
            for identifier, value in assignment.items():
                if value:
                    reconstructed = [
                        "1" if bit != delta else "0"
                        for bit, delta in zip(reconstructed, directions[identifier])
                    ]
            self.assertEqual("".join(reconstructed), assignment_conjunction(assignment))

        padded_base = satisfiability_padding_wrap(base, 17)
        padded_directions = {}
        for identifier in identifiers:
            unit = dict(zero_assignment)
            unit[identifier] = True
            padded_directions[identifier] = xor(
                padded_base,
                satisfiability_padding_wrap(assignment_conjunction(unit), 17),
            )
        self.assertEqual(
            satisfiability_padding_wrap(
                assignment_conjunction({4: True, 5: False, 6: True, 7: False}),
                17,
            ),
            "".join(
                str((int(base_bit) + int(d4) + int(d6)) % 2)
                for base_bit, d4, d6 in zip(
                    padded_base, padded_directions[4], padded_directions[6]
                )
            ),
        )


if __name__ == "__main__":
    unittest.main()
