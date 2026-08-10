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

    def test_radius_one_halo_schema_fresh_tail_counterexample(self) -> None:
        def bits(value: int, width: int) -> tuple[bool, ...]:
            return tuple(
                bool(value & (1 << (width - index - 1)))
                for index in range(width)
            )

        def row(
            edge: bool,
            context: int,
            width: int,
            position: int | None = None,
            coordinate: int | None = None,
        ) -> tuple[bool, ...]:
            blocks = [list(bits(context, width)) for _ in range(3)]
            if position is not None and coordinate is not None:
                blocks[position][coordinate] = not blocks[position][coordinate]
            return (edge, *(bit for block in blocks for bit in block))

        def ambient_base(
            prefix: tuple[bool, ...],
            y: tuple[bool, ...],
            auxiliary: tuple[bool, ...],
            witness: bool,
        ) -> bool:
            width = (len(prefix) - 1) // 3
            edge = prefix[0]
            blocks = tuple(
                prefix[1 + index * width:1 + (index + 1) * width]
                for index in range(3)
            )
            if blocks[0] == blocks[1] == blocks[2]:
                base_bits = blocks[0]
                position = None
            elif blocks[1] == blocks[2]:
                base_bits = blocks[1]
                position = 0
            elif blocks[0] == blocks[2]:
                base_bits = blocks[0]
                position = 1
            elif blocks[0] == blocks[1]:
                base_bits = blocks[0]
                position = 2
            else:
                return False

            context = sum(
                bit << (width - index - 1)
                for index, bit in enumerate(base_bits)
            )
            if position is None:
                return witness and (edge == y[context])

            outlier = blocks[position]
            differences = [
                index
                for index, pair in enumerate(zip(base_bits, outlier))
                if pair[0] != pair[1]
            ]
            if len(differences) != 1:
                return False
            coordinate = differences[0]
            neighbor = context ^ (1 << (width - coordinate - 1))
            table = {
                (True, 0): y[context]
                or (y[neighbor] and not auxiliary[context]),
                (True, 1): y[context],
                (True, 2): y[neighbor]
                or (y[context] and not auxiliary[context]),
                (False, 0): not y[context],
                (False, 1): (not y[context]) or (not y[neighbor]),
                (False, 2): not y[neighbor],
            }
            return witness and table[(edge, position)]

        for context_width in range(1, 5):
            context_count = 2**context_width
            seen = set()
            for context in range(context_count):
                for edge in (False, True):
                    cube_row = row(edge, context, context_width)
                    self.assertNotIn(cube_row, seen)
                    seen.add(cube_row)
                    for coordinate in range(context_width):
                        for position in range(3):
                            halo_row = row(
                                edge,
                                context,
                                context_width,
                                position,
                                coordinate,
                            )
                            self.assertNotIn(halo_row, seen)
                            seen.add(halo_row)

            expected_count = 2 * context_count * (1 + 3 * context_width)
            self.assertEqual(len(seen), expected_count)

        for context_width in (1, 2):
            context_count = 2**context_width
            suffixes = itertools.product(
                (False, True), repeat=2 * context_count + 1
            )
            for suffix in suffixes:
                y = suffix[:context_count]
                auxiliary = suffix[context_count:2 * context_count]
                witness = suffix[-1]
                for context in range(context_count):
                    for edge in (False, True):
                        self.assertEqual(
                            ambient_base(
                                row(edge, context, context_width),
                                y,
                                auxiliary,
                                witness,
                            ),
                            witness and (edge == y[context]),
                        )
                    for coordinate in range(context_width):
                        neighbor = context ^ (
                            1 << (context_width - coordinate - 1)
                        )
                        expected = {
                            (True, 0): witness
                            and (y[context] or (y[neighbor] and not auxiliary[context])),
                            (True, 1): witness and y[context],
                            (True, 2): witness
                            and (y[neighbor] or (y[context] and not auxiliary[context])),
                            (False, 0): witness and not y[context],
                            (False, 1): witness
                            and ((not y[context]) or (not y[neighbor])),
                            (False, 2): witness and not y[neighbor],
                        }
                        for edge in (False, True):
                            for position in range(3):
                                self.assertEqual(
                                    ambient_base(
                                        row(
                                            edge,
                                            context,
                                            context_width,
                                            position,
                                            coordinate,
                                        ),
                                        y,
                                        auxiliary,
                                        witness,
                                    ),
                                    expected[(edge, position)],
                                )
                        self.assertEqual(
                            expected[(False, 1)],
                            (witness and not y[context])
                            or (witness and not y[neighbor]),
                        )
                        self.assertEqual(
                            expected[(True, 0)],
                            (witness and y[context])
                            or (
                                witness
                                and y[neighbor]
                                and not auxiliary[context]
                            ),
                        )
                        self.assertEqual(
                            expected[(True, 2)],
                            (witness and y[neighbor])
                            or (
                                witness
                                and y[context]
                                and not auxiliary[context]
                            ),
                        )

            for tail_count in range(2, 5):
                reduced_suffixes = tuple(
                    itertools.product(
                        (False, True), repeat=context_count + 1 + tail_count
                    )
                )
                for context in range(context_count):
                    traces = set()
                    for edge in (False, True):
                        branch_traces = [[] for _ in range(tail_count)]
                        for suffix in reduced_suffixes:
                            y = suffix[:context_count]
                            witness = suffix[context_count]
                            tail = suffix[context_count + 1:]
                            value = witness and (edge == y[context])
                            for index, tail_bit in enumerate(tail):
                                value = value and tail_bit
                                branch_traces[index].append(value)
                        traces.update(map(tuple, branch_traces))
                    self.assertEqual(len(traces), 2 * tail_count)

    def test_ternary_witness_columns_admit_fresh_tail(self) -> None:
        def base(
            edge: bool,
            first: int,
            middle: int,
            final: int,
            low_x: tuple[bool, ...],
            high_x: tuple[bool, ...],
            low_u: tuple[bool, ...],
            high_u: tuple[bool, ...],
        ) -> bool:
            valid = all(
                low or high
                for low, high in zip(low_x + low_u, high_x + high_u)
            )
            if edge:
                feasible = high_x[final] or (
                    high_x[first] and low_u[middle]
                )
            else:
                feasible = low_x[final] or (
                    high_x[first] and low_x[middle]
                )
            return valid and feasible

        for context_width in (1, 2):
            context_count = 2**context_width
            observed = set()
            for supports in itertools.product(
                ((False,), (True,), (False, True)), repeat=context_count
            ):
                low_x = tuple(False in support for support in supports)
                high_x = tuple(True in support for support in supports)
                low_u = (True,) * context_count
                high_u = (True,) * context_count
                column = tuple(
                    base(
                        edge,
                        context,
                        context,
                        context,
                        low_x,
                        high_x,
                        low_u,
                        high_u,
                    )
                    for context in range(context_count)
                    for edge in (False, True)
                )
                observed.add(column)
            self.assertEqual(len(observed), 3**context_count)

            for x_values in itertools.product(
                (False, True), repeat=context_count
            ):
                for u_values in itertools.product(
                    (False, True), repeat=context_count
                ):
                    low_x = tuple(not value for value in x_values)
                    high_x = x_values
                    low_u = tuple(not value for value in u_values)
                    high_u = u_values
                    for first, middle, final in itertools.product(
                        range(context_count), repeat=3
                    ):
                        self.assertEqual(
                            base(
                                True,
                                first,
                                middle,
                                final,
                                low_x,
                                high_x,
                                low_u,
                                high_u,
                            ),
                            (x_values[first] and not u_values[middle])
                            or x_values[final],
                        )
                        self.assertEqual(
                            base(
                                False,
                                first,
                                middle,
                                final,
                                low_x,
                                high_x,
                                low_u,
                                high_u,
                            ),
                            (x_values[first] and not x_values[middle])
                            or not x_values[final],
                        )

        context_count = 2
        for tail_count in range(2, 5):
            suffixes = tuple(
                itertools.product((False, True), repeat=8 + tail_count)
            )
            for context in range(context_count):
                traces = set()
                branch_outputs = {}
                for edge in (False, True):
                    branch_traces = [[] for _ in range(tail_count)]
                    outputs = []
                    for suffix in suffixes:
                        low_x = suffix[0:2]
                        high_x = suffix[2:4]
                        low_u = suffix[4:6]
                        high_u = suffix[6:8]
                        tail = suffix[8:]
                        value = base(
                            edge,
                            context,
                            context,
                            context,
                            low_x,
                            high_x,
                            low_u,
                            high_u,
                        )
                        for index, tail_bit in enumerate(tail):
                            value = value and tail_bit
                            branch_traces[index].append(value)
                        outputs.append(value)
                    traces.update(map(tuple, branch_traces))
                    branch_outputs[edge] = tuple(outputs)
                self.assertEqual(len(traces), 2 * tail_count)
                common_union = tuple(
                    left or right
                    for left, right in zip(
                        branch_outputs[False], branch_outputs[True]
                    )
                )
                expected_union = []
                for suffix in suffixes:
                    valid = all(
                        low or high
                        for low, high in zip(
                            suffix[0:2] + suffix[4:6],
                            suffix[2:4] + suffix[6:8],
                        )
                    )
                    expected_union.append(valid and all(suffix[8:]))
                self.assertEqual(common_union, tuple(expected_union))


if __name__ == "__main__":
    unittest.main()
