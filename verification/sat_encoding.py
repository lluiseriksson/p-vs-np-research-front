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
