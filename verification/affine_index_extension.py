from __future__ import annotations

from dataclasses import dataclass
from math import ceil, log2
from typing import Iterable


Wire = tuple[str, int]


@dataclass(frozen=True)
class Gate:
    op: str
    inputs: tuple[Wire, ...]


@dataclass(frozen=True)
class Circuit:
    input_count: int
    gates: tuple[Gate, ...]
    output: Wire

    def evaluate(self, bits: tuple[bool, ...]) -> bool:
        if len(bits) != self.input_count:
            raise ValueError("wrong input length")
        values: list[bool] = []

        def value(wire: Wire) -> bool:
            kind, index = wire
            return bits[index] if kind == "input" else values[index]

        for gate in self.gates:
            arguments = tuple(value(wire) for wire in gate.inputs)
            if gate.op == "NOT":
                values.append(not arguments[0])
            elif gate.op == "AND":
                values.append(arguments[0] and arguments[1])
            elif gate.op == "OR":
                values.append(arguments[0] or arguments[1])
            else:
                raise ValueError(f"unknown operation: {gate.op}")
        return value(self.output)

    def depth(self) -> int:
        depths: list[int] = []

        def wire_depth(wire: Wire) -> int:
            kind, index = wire
            return 0 if kind == "input" else depths[index]

        for gate in self.gates:
            depths.append(1 + max(wire_depth(wire) for wire in gate.inputs))
        return wire_depth(self.output)

    def evaluate_gate_values(self, bits: tuple[bool, ...]) -> tuple[bool, ...]:
        if len(bits) != self.input_count:
            raise ValueError("wrong input length")
        values: list[bool] = []

        def value(wire: Wire) -> bool:
            kind, index = wire
            return bits[index] if kind == "input" else values[index]

        for gate in self.gates:
            arguments = tuple(value(wire) for wire in gate.inputs)
            if gate.op == "NOT":
                values.append(not arguments[0])
            elif gate.op == "AND":
                values.append(arguments[0] and arguments[1])
            elif gate.op == "OR":
                values.append(arguments[0] or arguments[1])
            else:
                raise ValueError(f"unknown operation: {gate.op}")
        return tuple(values)


def _reduce(gates: list[Gate], op: str, wires: Iterable[Wire]) -> Wire:
    level = list(wires)
    if not level:
        raise ValueError("cannot reduce an empty wire collection")
    while len(level) > 1:
        next_level: list[Wire] = []
        for index in range(0, len(level), 2):
            if index + 1 == len(level):
                next_level.append(level[index])
                continue
            gates.append(Gate(op, (level[index], level[index + 1])))
            next_level.append(("gate", len(gates) - 1))
        level = next_level
    return level[0]


def affine_index_extension(
    prefix_rows: dict[tuple[int, bool], str],
    base: str,
    directions: dict[int, str],
) -> Circuit:
    identifiers = tuple(sorted(directions))
    if not identifiers or set(prefix_rows) != {
        (identifier, bit) for identifier in identifiers for bit in (False, True)
    }:
        raise ValueError("rows must contain both polarities for every direction")
    row_values = tuple(prefix_rows.values())
    if len(set(row_values)) != len(row_values):
        raise ValueError("prefix rows must be distinct")
    prefix_widths = {len(row) for row in row_values}
    if len(prefix_widths) != 1 or next(iter(prefix_widths)) == 0:
        raise ValueError("prefix rows must have one positive common width")
    if any(bit not in "01" for row in row_values for bit in row):
        raise ValueError("prefix rows must be binary")
    if not base or any(bit not in "01" for bit in base):
        raise ValueError("base must be a nonempty binary string")
    if any(len(direction) != len(base) for direction in directions.values()):
        raise ValueError("directions must have the base length")

    supports = {
        identifier: {index for index, bit in enumerate(direction) if bit == "1"}
        for identifier, direction in directions.items()
    }
    if any(not support for support in supports.values()):
        raise ValueError("directions must be nonzero")
    occupied: set[int] = set()
    for identifier in identifiers:
        if occupied & supports[identifier]:
            raise ValueError("direction supports must be disjoint")
        occupied |= supports[identifier]

    p = next(iter(prefix_widths))
    gates: list[Gate] = []
    prefix_inputs = [("input", index) for index in range(p)]
    prefix_negations: list[Wire] = []
    for wire in prefix_inputs:
        gates.append(Gate("NOT", (wire,)))
        prefix_negations.append(("gate", len(gates) - 1))

    coordinate_literals: dict[tuple[int, bool], Wire] = {}
    for identifier in identifiers:
        pivot = min(supports[identifier])
        suffix_wire: Wire = ("input", p + pivot)
        gates.append(Gate("NOT", (suffix_wire,)))
        negated_wire: Wire = ("gate", len(gates) - 1)
        a_wire = suffix_wire if base[pivot] == "0" else negated_wire
        not_a_wire = negated_wire if base[pivot] == "0" else suffix_wire
        coordinate_literals[(identifier, True)] = a_wire
        coordinate_literals[(identifier, False)] = not_a_wire

    terms: list[Wire] = []
    for identifier in identifiers:
        for polarity in (False, True):
            row = prefix_rows[(identifier, polarity)]
            equality = _reduce(
                gates,
                "AND",
                (
                    prefix_inputs[index]
                    if bit == "1"
                    else prefix_negations[index]
                    for index, bit in enumerate(row)
                ),
            )
            gates.append(
                Gate("AND", (equality, coordinate_literals[(identifier, polarity)]))
            )
            terms.append(("gate", len(gates) - 1))

    output = _reduce(gates, "OR", terms)
    return Circuit(p + len(base), tuple(gates), output)


def prefix_dependent_affine_index_extension(
    prefix_rows: dict[tuple[int, bool], str],
) -> tuple[Circuit, str, dict[int, str]]:
    identifiers = tuple(sorted({identifier for identifier, _ in prefix_rows}))
    if not identifiers or set(prefix_rows) != {
        (identifier, bit) for identifier in identifiers for bit in (False, True)
    }:
        raise ValueError("rows must contain both polarities for every identifier")
    row_values = tuple(prefix_rows.values())
    if len(set(row_values)) != len(row_values):
        raise ValueError("prefix rows must be distinct")
    widths = {len(row) for row in row_values}
    if len(widths) != 1 or next(iter(widths)) == 0:
        raise ValueError("prefix rows must have one positive common width")
    if any(bit not in "01" for row in row_values for bit in row):
        raise ValueError("prefix rows must be binary")

    p = next(iter(widths))
    base_blocks = ["0011" for _ in identifiers]
    base = "".join(base_blocks)
    directions = {
        identifier: "0000" * index
        + "1111"
        + "0000" * (len(identifiers) - index - 1)
        for index, identifier in enumerate(identifiers)
    }

    gates: list[Gate] = []
    prefix_inputs = [("input", index) for index in range(p)]
    prefix_negations: list[Wire] = []
    for wire in prefix_inputs:
        gates.append(Gate("NOT", (wire,)))
        prefix_negations.append(("gate", len(gates) - 1))

    terms: list[Wire] = []
    for identifier_index, identifier in enumerate(identifiers):
        for polarity in (False, True):
            row = prefix_rows[(identifier, polarity)]
            equality = _reduce(
                gates,
                "AND",
                (
                    prefix_inputs[index]
                    if bit == "1"
                    else prefix_negations[index]
                    for index, bit in enumerate(row)
                ),
            )
            block_start = p + 4 * identifier_index
            target_start = block_start if polarity else block_start + 2
            gates.append(Gate("AND", (equality, ("input", target_start))))
            first = ("gate", len(gates) - 1)
            gates.append(Gate("AND", (first, ("input", target_start + 1))))
            terms.append(("gate", len(gates) - 1))

    output = _reduce(gates, "OR", terms)
    return Circuit(p + len(base), tuple(gates), output), base, directions


def prefix_dependent_gate_bound(identifier_count: int, prefix_width: int) -> int:
    if identifier_count < 1 or prefix_width < 1:
        raise ValueError("parameters must be positive")
    return 2 * identifier_count * prefix_width + 4 * identifier_count + prefix_width - 1


def prefix_dependent_depth_bound(identifier_count: int, prefix_width: int) -> int:
    if identifier_count < 1 or prefix_width < 1:
        raise ValueError("parameters must be positive")
    return 3 + ceil(log2(prefix_width)) + ceil(log2(2 * identifier_count))


def gate_bound(identifier_count: int, prefix_width: int) -> int:
    if identifier_count < 1 or prefix_width < 1:
        raise ValueError("parameters must be positive")
    return 2 * identifier_count * prefix_width + 3 * identifier_count + prefix_width - 1


def depth_bound(identifier_count: int, prefix_width: int) -> int:
    if identifier_count < 1 or prefix_width < 1:
        raise ValueError("parameters must be positive")
    return 2 + ceil(log2(prefix_width)) + ceil(log2(2 * identifier_count))
