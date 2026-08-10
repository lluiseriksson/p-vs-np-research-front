"""Reference implementation of the repository's exact SAT-gamma encoding.

This module parses iteratively so deeply nested prefix formulas remain total.
It verifies assignments; it does not attempt to solve SAT efficiently.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping


@dataclass(frozen=True)
class Node:
    op: str
    value: int | None = None
    children: tuple[int, ...] = ()


@dataclass(frozen=True)
class ParsedFormula:
    nodes: tuple[Node, ...]
    root: int
    variables: frozenset[int]


def encode_gamma(value: int) -> str:
    if value < 1:
        raise ValueError("gamma encoding requires a positive integer")
    binary = format(value, "b")
    return "0" * (len(binary) - 1) + binary


def decode_gamma(bits: str, position: int) -> tuple[int, int] | None:
    start = position
    while position < len(bits) and bits[position] == "0":
        position += 1
    if position >= len(bits):
        return None
    zeroes = position - start
    end = position + zeroes + 1
    if end > len(bits):
        return None
    word = bits[position:end]
    if not word or word[0] != "1":
        return None
    return int(word, 2), end


def encode_variable(identifier: int) -> str:
    return "00" + encode_gamma(identifier)


def encode_not(formula: str) -> str:
    return "11" + formula


def encode_and(left: str, right: str) -> str:
    return "01" + left + right


def encode_or(left: str, right: str) -> str:
    return "10" + left + right


def parse_formula(bits: str) -> ParsedFormula | None:
    if not bits or any(bit not in "01" for bit in bits):
        return None

    nodes: list[Node] = []
    variables: set[int] = set()
    frames: list[tuple[str, int, list[int]]] = []
    root: int | None = None
    position = 0

    def complete(node_index: int) -> None:
        nonlocal root
        while True:
            if not frames:
                if root is not None:
                    raise ValueError("multiple roots")
                root = node_index
                return
            op, arity, children = frames[-1]
            children.append(node_index)
            if len(children) < arity:
                return
            frames.pop()
            nodes.append(Node(op=op, children=tuple(children)))
            node_index = len(nodes) - 1

    try:
        while root is None:
            if position + 2 > len(bits):
                return None
            token = bits[position : position + 2]
            position += 2
            if token == "00":
                decoded = decode_gamma(bits, position)
                if decoded is None:
                    return None
                identifier, position = decoded
                variables.add(identifier)
                nodes.append(Node(op="VAR", value=identifier))
                complete(len(nodes) - 1)
            elif token == "01":
                frames.append(("AND", 2, []))
            elif token == "10":
                frames.append(("OR", 2, []))
            else:
                frames.append(("NOT", 1, []))
    except ValueError:
        return None

    if frames or position != len(bits) or root is None:
        return None
    return ParsedFormula(tuple(nodes), root, frozenset(variables))


def evaluate(parsed: ParsedFormula, assignment: Mapping[int, bool]) -> bool:
    values: list[bool] = []
    for node in parsed.nodes:
        if node.op == "VAR":
            if node.value not in assignment:
                raise KeyError(f"missing variable {node.value}")
            values.append(bool(assignment[node.value]))
        elif node.op == "NOT":
            values.append(not values[node.children[0]])
        elif node.op == "AND":
            values.append(values[node.children[0]] and values[node.children[1]])
        elif node.op == "OR":
            values.append(values[node.children[0]] or values[node.children[1]])
        else:
            raise ValueError(f"unknown operation {node.op}")
    return values[parsed.root]


def verify_assignment(bits: str, assignment: Mapping[int, bool]) -> bool:
    parsed = parse_formula(bits)
    return parsed is not None and evaluate(parsed, assignment)


def double_not_wrap(bits: str, count: int = 1) -> str:
    if count < 0:
        raise ValueError("count must be nonnegative")
    return "1111" * count + bits


def tautology(identifier: int = 1) -> str:
    variable = encode_variable(identifier)
    return encode_or(variable, encode_not(variable))


def contradiction(identifier: int = 1) -> str:
    variable = encode_variable(identifier)
    return encode_and(variable, encode_not(variable))


def context_wrap(
    bits: str,
    *,
    left_tautologies: int = 0,
    double_nots: int = 0,
) -> str:
    """Prefix ``bits`` with an exact satisfiability-preserving context.

    The source is the final literal substring.  If ``l`` and ``d`` are the two
    counts, its zero-based start is ``12*l + 4*d``.
    """
    if min(left_tautologies, double_nots) < 0:
        raise ValueError("context counts must be nonnegative")

    result = bits
    true_formula = tautology()
    for _ in range(left_tautologies):
        result = encode_and(true_formula, result)
    return double_not_wrap(result, double_nots)


def context_prefix(*, left_tautologies: int = 0, double_nots: int = 0) -> str:
    """Return only the fixed prefix used by :func:`context_wrap`."""
    return context_wrap(
        "",
        left_tautologies=left_tautologies,
        double_nots=double_nots,
    )


def annihilating_prefix(identifier: int = 1) -> str:
    """Prefix for ``AND(false, hole)``, whose SAT residual is constant zero."""
    return "01" + contradiction(identifier)


def operator_square_prefix(token: str, identifier: int = 1) -> str:
    """Twelve-bit prefix obtained by varying the inner two-bit operator."""
    if token not in {"00", "01", "10", "11"}:
        raise ValueError("token must be one of 00, 01, 10, 11")
    variable = encode_variable(identifier)
    return "01" + token + variable + encode_not(variable)


def conditioned_formula(value: bool, identifier: int = 1) -> str:
    """A twelve-bit formula equivalent to variable ``identifier`` or its NOT."""
    variable = encode_variable(identifier)
    if value:
        return double_not_wrap(encode_and(variable, variable))
    negated = encode_not(variable)
    return encode_and(negated, negated)


def conditioned_prefix(value: bool, identifier: int = 1) -> str:
    """Fourteen-bit prefix for AND(conditioned literal, hole)."""
    return "01" + conditioned_formula(value, identifier)


def one_bit_literal_gadgets(identifier: int) -> dict[bool, str]:
    """Return exact positive/negative literal formulas at Hamming distance one.

    The general construction applies when the identifier's binary expansion
    begins with ``11``.  Identifier 1 has the separate base construction with
    auxiliary identifier 3.
    """
    if identifier < 1:
        raise ValueError("identifier must be positive")
    binary = format(identifier, "b")
    if identifier == 1:
        auxiliary = 3
    elif binary.startswith("11"):
        auxiliary = int("1" + binary[2:] + "11", 2)
    else:
        raise ValueError("identifier must be 1 or have a binary code beginning 11")

    variable = encode_variable(identifier)
    auxiliary_variable = encode_variable(auxiliary)
    positive = encode_or(
        encode_and(variable, encode_not(auxiliary_variable)),
        variable,
    )
    negative = encode_or(
        encode_and(variable, encode_not(variable)),
        encode_not(variable),
    )
    return {True: positive, False: negative}


def one_bit_conditioned_prefix(value: bool, identifier: int) -> str:
    """Prefix for AND(one-bit literal gadget, hole)."""
    return "01" + one_bit_literal_gadgets(identifier)[value]


def assignment_conjunction(assignment: Mapping[int, bool]) -> str:
    """Encode an equal-polarity-length conjunction fixing every identifier.

    The true and false gadgets for a fixed identifier have equal length, so
    all assignments on the same identifier set produce formulas of one common
    length.
    """
    if not assignment:
        raise ValueError("assignment must be nonempty")
    items = sorted(assignment.items())
    result = conditioned_formula(items[0][1], items[0][0])
    for identifier, value in items[1:]:
        result = encode_and(result, conditioned_formula(value, identifier))
    return result


def satisfiability_padding_wrap(bits: str, extra_length: int) -> str:
    """Add exactly ``extra_length`` bits while preserving satisfiability.

    This uses double negations (+4) and conjunctions with positive variable 1
    (+5).  Semantic preservation requires identifier 1 to be fresh in the
    source and in any separately forced condition.
    """
    if extra_length < 12:
        raise ValueError("extra_length must be at least 12")
    five_count = extra_length % 4
    remainder = extra_length - 5 * five_count
    if remainder < 0 or remainder % 4:
        raise ValueError("extra_length is not representable by 4 and 5")
    result = double_not_wrap(bits, remainder // 4)
    fresh_variable = encode_variable(1)
    for _ in range(five_count):
        result = encode_and(fresh_variable, result)
    return result


def neutral_prefix_family(k: int) -> tuple[str, ...]:
    """The k+1 exact neutral prefixes of common length 12*k.

    Member ``l`` uses ``l`` tautology conjunctions and ``3*(k-l)`` double
    negations.
    """
    if k < 0:
        raise ValueError("k must be nonnegative")
    return tuple(
        context_prefix(left_tautologies=l, double_nots=3 * (k - l))
        for l in range(k + 1)
    )


def neutral_prefix_index(bits: str) -> int | None:
    """Return the family index of a neutral prefix, or ``None``.

    The input is split into twelve-bit blocks.  Neutral prefixes are exactly a
    run of all-one blocks followed by a run of ``01T`` blocks.
    """
    if len(bits) % 12 != 0 or any(bit not in "01" for bit in bits):
        return None
    all_one = "1" * 12
    context_block = context_prefix(left_tautologies=1)
    seen_context = False
    index = 0
    for start in range(0, len(bits), 12):
        block = bits[start : start + 12]
        if block == context_block:
            seen_context = True
            index += 1
        elif block == all_one and not seen_context:
            continue
        else:
            return None
    return index
