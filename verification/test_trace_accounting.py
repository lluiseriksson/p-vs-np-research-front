from __future__ import annotations

import itertools
import unittest


class FullTraceAccountingTests(unittest.TestCase):
    def test_lemma_026_audit_exposes_stable_core_collisions(self) -> None:
        independent = {"g", "h"}
        dependent_by_label = [set(), {"g"}, {"g_or_h", "h"}]
        dependent = set().union(*dependent_by_label)
        independent_count = 2
        dependent_count = 3
        alpha = independent_count - len(independent)
        z = sum(not residuals for residuals in dependent_by_label)
        t = sum(len(residuals) == 2 for residuals in dependent_by_label)
        kappa = sum(map(len, dependent_by_label)) - len(dependent)
        stable_collision = len(independent & dependent)
        quotient_size = len(independent | dependent)
        self.assertEqual(
            independent_count + dependent_count - quotient_size,
            alpha + z - t + kappa + stable_collision,
        )
        self.assertEqual(stable_collision, 2)

    def test_split_output_circuit_has_no_prefix_independent_gate(self) -> None:
        def trace(x: bool, y1: bool, y2: bool, w1: bool, w2: bool) -> tuple[bool, ...]:
            n = not x
            a1 = x or y1
            a2 = x or y2
            upper = a1 and a2
            b1 = n or w1
            b2 = n or w2
            lower = b1 and b2
            output = upper and lower
            return n, a1, a2, upper, b1, b2, lower, output

        suffixes = tuple(itertools.product((False, True), repeat=4))
        traces = {
            x: tuple(trace(x, *suffix) for suffix in suffixes)
            for x in (False, True)
        }
        for gate_index in range(8):
            self.assertNotEqual(
                tuple(row[gate_index] for row in traces[False]),
                tuple(row[gate_index] for row in traces[True]),
            )
        self.assertEqual(
            tuple(row[-1] for row in traces[False]),
            tuple(y1 and y2 for y1, y2, _, _ in suffixes),
        )
        self.assertEqual(
            tuple(row[-1] for row in traces[True]),
            tuple(w1 and w2 for _, _, w1, w2 in suffixes),
        )


if __name__ == "__main__":
    unittest.main()
