"""Reference implementation of the repository's exact SAT-gamma encoding.

This module parses iteratively so deeply nested prefix formulas remain total.
It verifies assignments; it does not attempt to solve SAT efficiently.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
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


def one_bit_auxiliary_identifier(identifier: int) -> int:
    """Return the auxiliary identifier in the exact one-bit gadget.

    The main affine family uses identifiers whose binary expansion begins
    with ``11``.  Identifier 1 is retained for the separate base gadget.
    """
    if identifier < 1:
        raise ValueError("identifier must be positive")
    binary = format(identifier, "b")
    if identifier == 1:
        return 3
    if binary.startswith("11"):
        return int("1" + binary[2:] + "11", 2)
    raise ValueError("identifier must be 1 or have a binary code beginning 11")


def one_bit_literal_gadgets(identifier: int) -> dict[bool, str]:
    """Return exact positive/negative literal formulas at Hamming distance one.

    The general construction applies when the identifier's binary expansion
    begins with ``11``.  Identifier 1 has the separate base construction with
    auxiliary identifier 3.
    """
    auxiliary = one_bit_auxiliary_identifier(identifier)

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


def one_bit_context_cube_prefix(
    value: bool,
    first_identifier: int,
    middle_identifier: int,
    final_identifier: int,
) -> str:
    """Vary the three repeated ENC-014 context blocks independently."""
    identifiers = (first_identifier, middle_identifier, final_identifier)
    binaries = tuple(format(identifier, "b") for identifier in identifiers)
    if len({len(binary) for binary in binaries}) != 1 or any(
        len(binary) < 2 or not binary.startswith("11") for binary in binaries
    ):
        raise ValueError(
            "identifiers must have one common bit length and binary form 11s"
        )

    first = encode_variable(first_identifier)
    final = encode_variable(final_identifier)
    if value:
        middle = encode_variable(
            one_bit_auxiliary_identifier(middle_identifier)
        )
        gadget = encode_or(encode_and(first, encode_not(middle)), final)
    else:
        middle = encode_variable(middle_identifier)
        gadget = encode_or(
            encode_and(first, encode_not(middle)),
            encode_not(final),
        )
    return "01" + gadget


def one_bit_halo_prefixes(
    value: bool,
    identifier: int,
    context_bit_index: int,
) -> dict[str, str]:
    """Return the three single-occurrence off-cube neighbors of a row.

    ``identifier`` must have binary form ``11s``.  A selected bit of ``s``
    occurs three times in the ENC-014 row.  The returned ``first``, ``middle``,
    and ``final`` prefixes toggle exactly one respective occurrence while
    retaining a well-formed formula with one suffix hole.
    """
    binary = format(identifier, "b")
    if len(binary) < 3 or not binary.startswith("11"):
        raise ValueError("identifier must have binary form 11s with nonempty s")
    context_width = len(binary) - 2
    if context_bit_index < 0 or context_bit_index >= context_width:
        raise ValueError("context_bit_index is outside the identifier context")

    toggled_identifier = identifier ^ (
        1 << (context_width - context_bit_index - 1)
    )
    return {
        "first": one_bit_context_cube_prefix(
            value, toggled_identifier, identifier, identifier
        ),
        "middle": one_bit_context_cube_prefix(
            value, identifier, toggled_identifier, identifier
        ),
        "final": one_bit_context_cube_prefix(
            value, identifier, identifier, toggled_identifier
        ),
    }


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


def common_outer_double_not_pad(
    bits: str,
    total_length: int,
    reserved_ones: int,
) -> str:
    """Pad to ``total_length`` with a shared all-one outer syntax block.

    ``reserved_ones`` must be a multiple of four, so the leading ones encode
    an even number of NOT tokens and preserve satisfiability.  Remaining
    length adjustment uses :func:`satisfiability_padding_wrap` inside it.
    """
    if reserved_ones < 0 or reserved_ones % 4:
        raise ValueError("reserved_ones must be a nonnegative multiple of four")
    inner_extra = total_length - reserved_ones - len(bits)
    if inner_extra < 12:
        raise ValueError("inner padding budget must be at least 12")
    inner = satisfiability_padding_wrap(bits, inner_extra)
    return double_not_wrap(inner, reserved_ones // 4)


def coordinate_dense_neutral_paddings(
    bits: str,
    extra_length: int,
) -> tuple[str, ...]:
    """Return equal-length neutral contexts varying every padding coordinate.

    The construction uses all-NOT padding and one tautology/contradiction
    context of length 12 or 16 placed at every compatible four-bit offset.
    It is exact for arbitrary source strings, including malformed strings.
    """
    if extra_length < 16 or extra_length % 4:
        raise ValueError("extra_length must be a multiple of four at least 16")

    blocks = (
        "01" + tautology(1),
        "10" + contradiction(1),
        "01" + tautology(2),
        "10" + contradiction(2),
    )
    contexts = {"1" * extra_length}
    for block in blocks:
        for start in range(0, extra_length - len(block) + 1, 4):
            contexts.add(
                "1" * start
                + block
                + "1" * (extra_length - start - len(block))
            )
    return tuple(sorted(context + bits for context in contexts))


def coordinate_dense_distant_pairs(
    extra_length: int,
) -> tuple[tuple[int, int], ...]:
    """Pair the two halves of an ENC-020 outer context.

    For a four-divisible length at least 32, paired coordinates are at least
    16 positions apart.  Since every nontrivial ENC-020 member has all zero
    bits inside one block of length at most 16, no pair is simultaneously
    zero on any member.
    """
    if extra_length < 32 or extra_length % 4:
        raise ValueError("extra_length must be a multiple of four at least 32")
    half = extra_length // 2
    return tuple((position, position + half) for position in range(half))


@lru_cache(maxsize=None)
def _pair_zero_neutral_placements(
    extra_length: int,
) -> tuple[tuple[int, str, frozenset[int]], ...]:
    blocks = tuple(
        block
        for identifier in (1, 2, 4, 8, 16)
        for block in (
            "01" + tautology(identifier),
            "10" + contradiction(identifier),
        )
    )
    placements = []
    for block in blocks:
        for start in range(0, extra_length - len(block) + 1, 4):
            zeros = frozenset(
                start + offset
                for offset, bit in enumerate(block)
                if bit == "0"
            )
            placements.append((start, block, zeros))
    return tuple(placements)


def pair_zero_neutral_padding(
    bits: str,
    extra_length: int,
    left_position: int,
    right_position: int,
) -> str | None:
    """Return a one/two-block neutral context zeroing two coordinates.

    Blocks use identifiers 1, 2, 4, 8, and 16.  For four-divisible outer
    lengths at least 32, a context exists for every unordered coordinate pair
    except (0,1), (0,2), (1,3), and (2,3).
    """
    if extra_length < 32 or extra_length % 4:
        raise ValueError("extra_length must be a multiple of four at least 32")
    if not 0 <= left_position < extra_length:
        raise ValueError("left_position is outside the outer context")
    if not 0 <= right_position < extra_length:
        raise ValueError("right_position is outside the outer context")
    if left_position > right_position:
        left_position, right_position = right_position, left_position

    placements = _pair_zero_neutral_placements(extra_length)

    def assemble(selected: tuple[tuple[int, str, frozenset[int]], ...]) -> str:
        context = []
        cursor = 0
        for start, block, _ in sorted(selected):
            context.append("1" * (start - cursor))
            context.append(block)
            cursor = start + len(block)
        context.append("1" * (extra_length - cursor))
        return "".join(context) + bits

    for placement in placements:
        if left_position in placement[2] and right_position in placement[2]:
            return assemble((placement,))

    for left_placement in placements:
        if left_position not in left_placement[2]:
            continue
        left_start, left_block, _ = left_placement
        left_end = left_start + len(left_block)
        for right_placement in placements:
            if right_position not in right_placement[2]:
                continue
            right_start, right_block, _ = right_placement
            right_end = right_start + len(right_block)
            if left_end <= right_start or right_end <= left_start:
                return assemble((left_placement, right_placement))
    return None


def one_two_block_neutral_paddings(
    bits: str,
    extra_length: int,
) -> tuple[str, ...]:
    """Enumerate the ENC-022 one/two-block neutral context family."""
    if extra_length < 32 or extra_length % 4:
        raise ValueError("extra_length must be a multiple of four at least 32")
    placements = _pair_zero_neutral_placements(extra_length)

    def assemble(selected: tuple[tuple[int, str, frozenset[int]], ...]) -> str:
        context = []
        cursor = 0
        for start, block, _ in sorted(selected):
            context.append("1" * (start - cursor))
            context.append(block)
            cursor = start + len(block)
        context.append("1" * (extra_length - cursor))
        return "".join(context) + bits

    contexts = {assemble((placement,)) for placement in placements}
    for left_index, left in enumerate(placements):
        left_start, left_block, _ = left
        left_end = left_start + len(left_block)
        for right in placements[left_index + 1:]:
            right_start, right_block, _ = right
            right_end = right_start + len(right_block)
            if left_end <= right_start or right_end <= left_start:
                contexts.add(assemble((left, right)))
    return tuple(sorted(contexts))


def distant_outer_triples(
    extra_length: int,
) -> tuple[tuple[int, int, int], ...]:
    """Partition a 12-divisible outer region into separated triples."""
    if extra_length < 84 or extra_length % 12:
        raise ValueError("extra_length must be a multiple of twelve at least 84")
    third = extra_length // 3
    return tuple(
        (position, position + third, position + 2 * third)
        for position in range(third)
    )


def bounded_block_distant_groups(
    extra_length: int,
    block_count: int,
    max_block_length: int,
) -> tuple[tuple[int, ...], ...]:
    """Build the groups missed by a bounded number of short zero blocks."""
    if block_count < 0:
        raise ValueError("block_count must be nonnegative")
    if max_block_length < 1:
        raise ValueError("max_block_length must be positive")
    width = block_count + 1
    group_count = extra_length // width
    if group_count < max_block_length:
        raise ValueError("outer region is too short for separated groups")
    return tuple(
        tuple(position + offset * group_count for offset in range(width))
        for position in range(group_count)
    )


def maximum_zero_run(bits: str) -> int:
    """Return the maximum number of consecutive zero bits."""
    if any(bit not in "01" for bit in bits):
        raise ValueError("bits must be binary")
    return max((len(run) for run in bits.split("1")), default=0)


def bounded_zero_run_windows(
    extra_length: int,
    max_zero_run: int,
) -> tuple[tuple[int, ...], ...]:
    """Partition the usable prefix into OR windows longer than every zero run."""
    if max_zero_run < 0:
        raise ValueError("max_zero_run must be nonnegative")
    width = max_zero_run + 1
    window_count = extra_length // width
    return tuple(
        tuple(range(index * width, (index + 1) * width))
        for index in range(window_count)
    )


def power_two_long_zero_neutral_block(zero_run: int) -> str:
    """Return a length-4r exact neutral block with maximum zero run r."""
    if zero_run < 3:
        raise ValueError("zero_run must be at least three")
    identifier = 1 << (zero_run - 3)
    return "01" + tautology(identifier)


def long_zero_window_neutral_padding(
    bits: str,
    extra_length: int,
    zero_run: int,
    window_start: int,
    window_length: int,
) -> str:
    """Place a tunable neutral block so its leading run covers a window."""
    block = power_two_long_zero_neutral_block(zero_run)
    if extra_length < len(block):
        raise ValueError("extra_length is shorter than the neutral block")
    if extra_length % 4:
        raise ValueError("extra_length must be divisible by four")
    if window_length < 0 or window_length > zero_run - 3:
        raise ValueError("window_length exceeds the sweep guarantee")
    if window_start < 3 or window_start > extra_length - len(block) + 3:
        raise ValueError("window_start is outside the swept interior")
    run_start = window_start - ((window_start - 3) % 4)
    block_start = run_start - 3
    if window_start + window_length > run_start + zero_run:
        raise AssertionError("chosen zero run does not cover the window")
    return (
        "1" * block_start
        + block
        + "1" * (extra_length - block_start - len(block))
        + bits
    )


def balanced_long_run_slot_options(zero_run: int) -> tuple[str, ...]:
    """Return coordinate-dense short contexts plus one tunable long block."""
    if zero_run < 7:
        raise ValueError("zero_run must be at least seven")
    slot_length = 4 * zero_run
    options = set(coordinate_dense_neutral_paddings("", slot_length))
    options.add(power_two_long_zero_neutral_block(zero_run))
    return tuple(sorted(options))


def balanced_common_implication_pairs(
    zero_run: int,
) -> tuple[tuple[int, int], ...]:
    """Return a large disjoint family of common mixed two-clauses.

    A pair ``(positive, negative)`` denotes the clause
    ``z_positive OR NOT z_negative``.  The two candidate pairs in each
    aligned four-bit chunk partition the slot coordinates; candidates
    falsified by the tunable long block are omitted.
    """
    options = balanced_long_run_slot_options(zero_run)
    pairs = []
    for chunk in range(zero_run):
        start = 4 * chunk
        for positive, negative in (
            (start + 3, start),
            (start + 2, start + 1),
        ):
            if all(
                option[positive] == "1" or option[negative] == "0"
                for option in options
            ):
                pairs.append((positive, negative))
    return tuple(pairs)


def implication_sparse_long_run_slot_options(
    zero_run: int,
) -> tuple[str, ...]:
    """Return balanced options plus all placements of ``A_7,...,A_12``.

    The fixed translated long blocks destroy every common mixed two-clause
    outside constant-size boundary regions while ``A_zero_run`` retains the
    tunable run required by the outer construction.
    """
    if zero_run < 13:
        raise ValueError("zero_run must be at least thirteen")
    slot_length = 4 * zero_run
    options = set(balanced_long_run_slot_options(zero_run))
    for short_run in range(7, 13):
        block = power_two_long_zero_neutral_block(short_run)
        for start in range(0, slot_length - len(block) + 1, 4):
            options.add(
                "1" * start
                + block
                + "1" * (slot_length - start - len(block))
            )
    return tuple(sorted(options))


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
