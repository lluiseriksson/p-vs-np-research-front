"""Small exact certificates for aligned bounded-interval gap reductions."""

from __future__ import annotations


def reached_zero_masks(
    blocks: tuple[str, ...],
    positions: tuple[int, ...],
    max_blocks: int,
    *,
    alignment: int = 4,
) -> frozenset[int]:
    """Enumerate zero masks from nonoverlapping aligned block placements."""
    if (
        not positions
        or positions != tuple(sorted(set(positions)))
        or positions[0] < 0
        or max_blocks < 0
        or alignment < 1
        or any(not block or set(block) - {"0", "1"} for block in blocks)
    ):
        raise ValueError("invalid blocks, positions, block budget, or alignment")
    length = positions[-1] + max(map(len, blocks), default=1) + alignment
    placements = []
    for block in blocks:
        for start in range(0, length - len(block) + 1, alignment):
            mask = sum(
                1 << bit
                for bit, position in enumerate(positions)
                if start <= position < start + len(block)
                and block[position - start] == "0"
            )
            if mask:
                placements.append((start, start + len(block), mask))

    reached = {0}

    def extend(previous_end: int, remaining: int, mask: int) -> None:
        reached.add(mask)
        if remaining == 0:
            return
        for start, end, placement_mask in placements:
            if start >= previous_end:
                extend(end, remaining - 1, mask | placement_mask)

    extend(0, max_blocks, 0)
    return frozenset(reached)


def unsafe_bound_gap_counterexample() -> tuple[frozenset[int], frozenset[int]]:
    """Return masks at congruent gaps 15 and 11 for the length-eight example."""
    blocks = ("01111111", "11111110")
    return (
        reached_zero_masks(blocks, (8, 23), 2),
        reached_zero_masks(blocks, (8, 19), 2),
    )
