"""Symbolic complete-identifier interval oracle for at most five coordinates."""

from __future__ import annotations

from functools import lru_cache


FIXED_ZERO = 0
FIXED_ONE = 1
VARIABLE_BASE = 2


@lru_cache(maxsize=None)
def symbolic_neutral_templates(
    max_free_bit_count: int,
) -> tuple[tuple[int, ...], ...]:
    """Return both neutral block templates for every included ID bit length."""
    if max_free_bit_count < 0:
        raise ValueError("maximum free bit count must be nonnegative")
    templates = []
    for free_bit_count in range(max_free_bit_count + 1):
        gamma = (
            (FIXED_ZERO,) * free_bit_count
            + (FIXED_ONE,)
            + tuple(
                VARIABLE_BASE + column
                for column in reversed(range(free_bit_count))
            )
        )
        variable = (FIXED_ZERO, FIXED_ZERO) + gamma
        suffix = variable + (FIXED_ONE, FIXED_ONE) + variable
        templates.append((FIXED_ZERO, FIXED_ONE, FIXED_ONE, FIXED_ZERO) + suffix)
        templates.append((FIXED_ONE, FIXED_ZERO, FIXED_ZERO, FIXED_ONE) + suffix)
    return tuple(templates)


def _mask_options(
    template: tuple[int, ...], start: int, positions: tuple[int, ...]
) -> tuple[int, ...]:
    fixed_mask = 0
    variable_groups: dict[int, int] = {}
    end = start + len(template)
    for bit, position in enumerate(positions):
        if not start <= position < end:
            continue
        token = template[position - start]
        if token == FIXED_ZERO:
            fixed_mask |= 1 << bit
        elif token >= VARIABLE_BASE:
            variable_groups[token] = variable_groups.get(token, 0) | (1 << bit)
    options = {fixed_mask}
    for group_mask in variable_groups.values():
        options |= {mask | group_mask for mask in tuple(options)}
    return tuple(options)


class CompleteIdentifierAuditor:
    """Audit every identifier through one bit length without enumerating IDs."""

    def __init__(self, max_free_bit_count: int, representative_length: int) -> None:
        self.max_free_bit_count = max_free_bit_count
        self.length = representative_length
        self.templates = symbolic_neutral_templates(max_free_bit_count)

    def reached_masks_positions(
        self, positions: tuple[int, ...], max_blocks: int
    ) -> int:
        if (
            not positions
            or len(positions) > 5
            or max_blocks < 1
            or positions != tuple(sorted(set(positions)))
            or positions[0] < 0
            or positions[-1] >= self.length
        ):
            raise ValueError("positions must be 1-5 strictly increasing coordinates")
        full_mask = (1 << len(positions)) - 1
        best_at_start: list[dict[int, int]] = [
            {} for _ in range(self.length + 1)
        ]
        for template in self.templates:
            block_length = len(template)
            for start in range(0, self.length - block_length + 1, 4):
                if start > positions[-1] or start + block_length <= positions[0]:
                    continue
                end = start + block_length
                for mask in _mask_options(template, start, positions):
                    if mask in (0, full_mask):
                        continue
                    previous = best_at_start[start].get(mask, self.length + 1)
                    if end < previous:
                        best_at_start[start][mask] = end

        next_from: list[dict[int, int]] = [
            {} for _ in range(self.length + 1)
        ]
        running: dict[int, int] = {}
        for threshold in range(self.length, -1, -1):
            for mask, end in best_at_start[threshold].items():
                if end < running.get(mask, self.length + 1):
                    running[mask] = end
            next_from[threshold] = running.copy()

        reached = 1
        frontier = {0: 0}
        target = (1 << full_mask) - 2
        for _ in range(max_blocks):
            following: dict[int, int] = {}
            for accumulated, previous_end in frontier.items():
                for mask, end in next_from[previous_end].items():
                    combined = accumulated | mask
                    if combined == full_mask:
                        continue
                    if end < following.get(combined, self.length + 1):
                        following[combined] = end
                    reached |= 1 << combined
            frontier = following
            if not frontier or reached & target == target:
                break
        return reached
