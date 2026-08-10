from __future__ import annotations

import collections
import itertools
import math
import unittest


class ExpandedContextIncidenceTests(unittest.TestCase):
    def test_exact_condition_class_counts_and_multiplicities(self) -> None:
        for context_count in range(2, 5):
            x_assignments = tuple(
                itertools.product((False, True), repeat=context_count)
            )
            xu_assignments = tuple(
                itertools.product((False, True), repeat=2 * context_count)
            )

            positive_classes: dict[tuple[bool, ...], list[tuple[int, int, int]]]
            positive_classes = collections.defaultdict(list)
            negative_classes: dict[tuple[bool, ...], list[tuple[int, int, int]]]
            negative_classes = collections.defaultdict(list)

            for first, middle, final in itertools.product(
                range(context_count), repeat=3
            ):
                positive = tuple(
                    (assignment[first] and not assignment[context_count + middle])
                    or assignment[final]
                    for assignment in xu_assignments
                )
                negative = tuple(
                    (assignment[first] and not assignment[middle])
                    or not assignment[final]
                    for assignment in x_assignments
                )
                positive_classes[positive].append((first, middle, final))
                negative_classes[negative].append((first, middle, final))

            expected_positive = (
                context_count**3 - context_count**2 + context_count
            )
            expected_negative = (
                context_count
                + math.comb(context_count, 2)
                + context_count * (context_count - 1) * (context_count - 2)
            )
            self.assertEqual(len(positive_classes), expected_positive)
            self.assertEqual(len(negative_classes), expected_negative)

            positive_multiplicities = collections.Counter(
                map(len, positive_classes.values())
            )
            self.assertEqual(positive_multiplicities[context_count], context_count)
            self.assertEqual(
                positive_multiplicities[1],
                context_count**2 * (context_count - 1),
            )

            negative_multiplicities = collections.Counter(
                map(len, negative_classes.values())
            )
            self.assertEqual(
                negative_multiplicities[2 * context_count - 1], context_count
            )
            self.assertEqual(
                negative_multiplicities[2], math.comb(context_count, 2)
            )
            if context_count >= 3:
                self.assertEqual(
                    negative_multiplicities[1],
                    context_count * (context_count - 1) * (context_count - 2),
                )

            negative_on_extended_domain = {
                tuple(
                    (assignment[first] and not assignment[middle])
                    or not assignment[final]
                    for assignment in (
                        extended[:context_count] for extended in xu_assignments
                    )
                )
                for first, middle, final in itertools.product(
                    range(context_count), repeat=3
                )
            }
            self.assertTrue(
                set(positive_classes).isdisjoint(negative_on_extended_domain)
            )

    def test_diagonal_conditioned_outputs_realize_ternary_patterns(self) -> None:
        for context_count in range(1, 6):
            observed = set()
            for supports in itertools.product(
                ((False,), (True,), (False, True)), repeat=context_count
            ):
                assignments = itertools.product(*supports)
                assignment_set = tuple(assignments)
                pattern = tuple(
                    value in {assignment[index] for assignment in assignment_set}
                    for index in range(context_count)
                    for value in (False, True)
                )
                observed.add(pattern)
            self.assertEqual(len(observed), 3**context_count)


if __name__ == "__main__":
    unittest.main()
