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
