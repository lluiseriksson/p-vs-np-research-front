"""Deterministic strength-five identifier basis for GATE-004AF."""

from __future__ import annotations

from functools import lru_cache
from hashlib import sha256
from itertools import combinations


FREE_COLUMNS = tuple(range(14))
FIVE_COLUMN_SUBSETS = tuple(combinations(FREE_COLUMNS, 5))


@lru_cache(maxsize=1)
def strength_five_identifier_basis() -> tuple[int, ...]:
    """Return explicit 15-bit IDs covering every pattern on five free bits."""
    uncovered = {
        (columns, pattern)
        for columns in FIVE_COLUMN_SUBSETS
        for pattern in range(32)
    }
    words: list[int] = []
    seen: set[int] = set()
    counter = 0
    while uncovered:
        digest = sha256(f"p-vs-np-width5-{counter}".encode("ascii")).digest()
        counter += 1
        word = int.from_bytes(digest[:2], "big") & 0x3FFF
        if word in seen:
            continue
        seen.add(word)
        words.append(word)
        for columns in FIVE_COLUMN_SUBSETS:
            pattern = sum(
                ((word >> column) & 1) << index
                for index, column in enumerate(columns)
            )
            uncovered.discard((columns, pattern))
    return tuple((1 << 14) | word for word in words)


def strength_five_coverage_failures(
    identifiers: tuple[int, ...],
) -> tuple[tuple[tuple[int, ...], int], ...]:
    """List missing five-column patterns in the fourteen free ID bits."""
    words = tuple(identifier ^ (1 << 14) for identifier in identifiers)
    failures = []
    for columns in FIVE_COLUMN_SUBSETS:
        reached = {
            sum(
                ((word >> column) & 1) << index
                for index, column in enumerate(columns)
            )
            for word in words
        }
        for pattern in range(32):
            if pattern not in reached:
                failures.append((columns, pattern))
    return tuple(failures)


@lru_cache(maxsize=None)
def identifier_projection_basis(free_bit_count: int) -> tuple[int, ...]:
    """Cover every assignment on up to five free bits at one ID length."""
    if not 0 <= free_bit_count <= 16:
        raise ValueError("free bit count must lie between zero and sixteen")
    if free_bit_count == 0:
        return (1,)
    strength = min(5, free_bit_count)
    column_subsets = tuple(combinations(range(free_bit_count), strength))
    uncovered = {
        (columns, pattern)
        for columns in column_subsets
        for pattern in range(1 << strength)
    }
    identifiers: list[int] = []
    seen: set[int] = set()
    counter = 0
    while uncovered:
        digest = sha256(
            f"p-vs-np-width5-n{free_bit_count}-{counter}".encode("ascii")
        ).digest()
        counter += 1
        word = int.from_bytes(digest[:4], "big") & ((1 << free_bit_count) - 1)
        if word in seen:
            continue
        seen.add(word)
        identifiers.append((1 << free_bit_count) | word)
        for columns in column_subsets:
            pattern = sum(
                ((word >> column) & 1) << index
                for index, column in enumerate(columns)
            )
            uncovered.discard((columns, pattern))
    return tuple(identifiers)


@lru_cache(maxsize=1)
def all_length_identifier_projection_basis() -> tuple[int, ...]:
    """Projection-complete representatives for every ID from 1 through 32767."""
    return tuple(
        identifier
        for free_bit_count in range(15)
        for identifier in identifier_projection_basis(free_bit_count)
    )


@lru_cache(maxsize=None)
def identifier_projection_basis_through(
    max_free_bit_count: int,
) -> tuple[int, ...]:
    if not 0 <= max_free_bit_count <= 16:
        raise ValueError("maximum free bit count must lie between zero and sixteen")
    return tuple(
        identifier
        for free_bit_count in range(max_free_bit_count + 1)
        for identifier in identifier_projection_basis(free_bit_count)
    )


def projection_coverage_failures(
    free_bit_count: int,
) -> tuple[tuple[tuple[int, ...], int], ...]:
    identifiers = identifier_projection_basis(free_bit_count)
    words = tuple(
        identifier ^ (1 << free_bit_count) for identifier in identifiers
    )
    strength = min(5, free_bit_count)
    failures = []
    for columns in combinations(range(free_bit_count), strength):
        reached = {
            sum(
                ((word >> column) & 1) << index
                for index, column in enumerate(columns)
            )
            for word in words
        }
        for pattern in range(1 << strength):
            if pattern not in reached:
                failures.append((columns, pattern))
    return tuple(failures)


def all_length_projection_coverage_failures() -> tuple[
    tuple[int, tuple[int, ...], int], ...
]:
    failures = []
    for free_bit_count in range(15):
        for columns, pattern in projection_coverage_failures(free_bit_count):
            failures.append((free_bit_count, columns, pattern))
    return tuple(failures)


def selected_position_projection_sets(
    free_bit_count: int,
    positions: tuple[int, ...],
    representative_length: int,
) -> tuple[tuple[int, ...], ...]:
    """Return the identifier-bit projections touched by relevant placements.

    This derives the two repeated gamma suffix locations directly from the
    literal block layout, independently of the symbolic-template oracle.
    """
    if free_bit_count < 0:
        raise ValueError("free bit count must be nonnegative")
    if (
        not positions
        or len(positions) > 5
        or positions != tuple(sorted(set(positions)))
        or positions[0] < 0
        or positions[-1] >= representative_length
    ):
        raise ValueError("positions must be 1-5 strictly increasing coordinates")
    block_length = 12 + 4 * free_bit_count
    projections = set()
    for start in range(0, representative_length - block_length + 1, 4):
        if start > positions[-1] or start + block_length <= positions[0]:
            continue
        columns = set()
        for position in positions:
            relative = position - start
            if free_bit_count + 7 <= relative <= 2 * free_bit_count + 6:
                columns.add(2 * free_bit_count + 6 - relative)
            elif 3 * free_bit_count + 12 <= relative <= 4 * free_bit_count + 11:
                columns.add(4 * free_bit_count + 11 - relative)
        projections.add(tuple(sorted(columns)))
    return tuple(sorted(projections))


@lru_cache(maxsize=None)
def identifier_projection_basis_for_positions(
    max_free_bit_count: int,
    positions: tuple[int, ...],
    representative_length: int,
) -> tuple[int, ...]:
    """Represent every relevant selected-coordinate behavior through a bound."""
    identifiers = set()
    for free_bit_count in range(max_free_bit_count + 1):
        for columns in selected_position_projection_sets(
            free_bit_count, positions, representative_length
        ):
            for pattern in range(1 << len(columns)):
                suffix = sum(
                    ((pattern >> index) & 1) << column
                    for index, column in enumerate(columns)
                )
                identifiers.add((1 << free_bit_count) | suffix)
    return tuple(sorted(identifiers))


def selected_position_projection_coverage_failures(
    max_free_bit_count: int,
    positions: tuple[int, ...],
    representative_length: int,
) -> tuple[tuple[int, tuple[int, ...], int], ...]:
    """Check the position-specific basis against every required projection."""
    basis = identifier_projection_basis_for_positions(
        max_free_bit_count, positions, representative_length
    )
    by_length = {
        free_bit_count: tuple(
            identifier ^ (1 << free_bit_count)
            for identifier in basis
            if identifier.bit_length() == free_bit_count + 1
        )
        for free_bit_count in range(max_free_bit_count + 1)
    }
    failures = []
    for free_bit_count in range(max_free_bit_count + 1):
        for columns in selected_position_projection_sets(
            free_bit_count, positions, representative_length
        ):
            reached = {
                sum(
                    ((word >> column) & 1) << index
                    for index, column in enumerate(columns)
                )
                for word in by_length[free_bit_count]
            }
            for pattern in range(1 << len(columns)):
                if pattern not in reached:
                    failures.append((free_bit_count, columns, pattern))
    return tuple(failures)
