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

    def test_minimum_context_chain_joint_quotient_count(self) -> None:
        for size in range(3, 9):
            suffixes = tuple(itertools.product((False, True), repeat=size))

            def gate_traces(context: bool) -> tuple[tuple[bool, ...], ...]:
                traces = [[] for _ in range(size)]
                for suffix in suffixes:
                    value = context or suffix[0]
                    traces[0].append(value)
                    for index in range(1, size):
                        value = value and suffix[index]
                        traces[index].append(value)
                return tuple(tuple(trace) for trace in traces)

            input_traces = {
                tuple(suffix[index] for suffix in suffixes)
                for index in range(size)
            }
            active = set()
            all_gate_traces = []
            for context in (False, True):
                for trace in gate_traces(context):
                    all_gate_traces.append(trace)
                    if trace in input_traces or len(set(trace)) == 1:
                        continue
                    active.add(trace)

            self.assertEqual(len(active), 2 * size - 3)
            self.assertEqual(size - len(active), 3 - size)
            for gate_index in range(size):
                self.assertNotEqual(
                    gate_traces(False)[gate_index],
                    gate_traces(True)[gate_index],
                )

    def test_one_hot_shattering_joint_quotient_count(self) -> None:
        for context_count in range(2, 5):
            for tail_count in range(3, 7):
                suffixes = tuple(
                    itertools.product(
                        (False, True), repeat=context_count + tail_count
                    )
                )
                input_traces = {
                    tuple(suffix[index] for suffix in suffixes)
                    for index in range(context_count + tail_count)
                }
                for context_index in range(context_count):
                    active = set()
                    for edge in (False, True):
                        traces = [[] for _ in range(tail_count + 1)]
                        for suffix in suffixes:
                            y = suffix[:context_count]
                            z = suffix[context_count:]
                            value = edge or y[context_index]
                            traces[0].append(value)
                            value = value or z[0]
                            traces[1].append(value)
                            for tail_index in range(1, tail_count):
                                value = value and z[tail_index]
                                traces[tail_index + 1].append(value)
                        for trace in map(tuple, traces):
                            if trace in input_traces or len(set(trace)) == 1:
                                continue
                            active.add(trace)

                    self.assertEqual(len(active), 2 * tail_count - 2)
                    parent_size = 2 * context_count + tail_count
                    self.assertEqual(
                        parent_size - len(active),
                        2 * context_count - tail_count + 2,
                    )

                observed_columns = set()
                for column in itertools.product((False, True), repeat=context_count):
                    observed_columns.add(tuple(column))
                self.assertEqual(len(observed_columns), 2**context_count)

    def test_compressed_cube_fresh_tail_counterexample(self) -> None:
        for context_width in (1, 2):
            context_count = 2**context_width
            for tail_count in range(2, 5):
                suffixes = tuple(
                    itertools.product(
                        (False, True), repeat=context_count + 1 + tail_count
                    )
                )
                for context in range(context_count):
                    active_tail_traces = set()
                    branch_outputs = {}
                    for edge in (False, True):
                        traces = [[] for _ in range(tail_count)]
                        outputs = []
                        for suffix in suffixes:
                            y = suffix[:context_count]
                            witness = suffix[context_count]
                            tail = suffix[context_count + 1:]
                            value = witness and (edge == y[context])
                            for index, tail_bit in enumerate(tail):
                                value = value and tail_bit
                                traces[index].append(value)
                            outputs.append(value)
                        branch_outputs[edge] = tuple(outputs)
                        active_tail_traces.update(map(tuple, traces))

                    self.assertEqual(len(active_tail_traces), 2 * tail_count)
                    common_union = tuple(
                        left or right
                        for left, right in zip(
                            branch_outputs[False], branch_outputs[True]
                        )
                    )
                    expected_union = tuple(
                        suffix[context_count]
                        and all(suffix[context_count + 1:])
                        for suffix in suffixes
                    )
                    self.assertEqual(common_union, expected_union)

                observed_columns = set()
                for assignment in itertools.product(
                    (False, True), repeat=context_count
                ):
                    column = tuple(
                        edge == assignment[context]
                        for context in range(context_count)
                        for edge in (False, True)
                    )
                    observed_columns.add(column)
                self.assertEqual(len(observed_columns), 2**context_count)


if __name__ == "__main__":
    unittest.main()
