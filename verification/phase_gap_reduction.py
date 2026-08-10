"""Exact zero-overhang parameters for phase-sensitive gap reductions."""

from __future__ import annotations

from sat_encoding import contradiction, tautology


def zero_overhangs(
    identifiers: tuple[int, ...],
) -> tuple[tuple[int, ...], tuple[int, ...]]:
    """Return maximum right/left overhangs at zero coordinates by residue."""
    right = [0] * 4
    left = [0] * 4
    for identifier in identifiers:
        for block in (
            "01" + tautology(identifier),
            "10" + contradiction(identifier),
        ):
            for offset, bit in enumerate(block):
                if bit != "0":
                    continue
                residue = offset % 4
                right[residue] = max(right[residue], len(block) - offset)
                left[residue] = max(left[residue], offset)
    return tuple(right), tuple(left)


def phase_gap_caps(
    identifiers: tuple[int, ...],
) -> tuple[int, ...]:
    """Return the largest required representative gap for each left residue."""
    right, left = zero_overhangs(identifiers)
    return tuple(
        max(right[source] + left[target] for target in range(4))
        for source in range(4)
    )


def reduced_type_counts(phase_caps: tuple[int, ...]) -> tuple[int, ...]:
    """Count three-gap types for each first-coordinate residue."""
    if len(phase_caps) != 4 or any(cap < 1 for cap in phase_caps):
        raise ValueError("phase caps must contain four positive integers")
    counts = []
    for residue in range(4):
        count = 0
        for gap_1 in range(1, phase_caps[residue] + 1):
            residue_1 = (residue + gap_1) % 4
            for gap_2 in range(1, phase_caps[residue_1] + 1):
                residue_2 = (residue_1 + gap_2) % 4
                count += phase_caps[residue_2]
        counts.append(count)
    return tuple(counts)


def reduce_phase_gaps(
    first_residue: int,
    gaps: tuple[int, ...],
    phase_caps: tuple[int, ...],
) -> tuple[int, ...]:
    """Normalize gaps by multiples of four while preserving every residue."""
    if first_residue not in range(4):
        raise ValueError("first residue must be 0, 1, 2, or 3")
    if len(phase_caps) != 4 or any(cap < 1 for cap in phase_caps):
        raise ValueError("phase caps must contain four positive integers")
    if any(gap < 1 for gap in gaps):
        raise ValueError("gaps must be positive")
    residue = first_residue
    reduced = []
    for gap in gaps:
        cap = phase_caps[residue]
        if gap > cap:
            gap -= 4 * ((gap - cap + 3) // 4)
        if not 1 <= gap <= cap:
            raise AssertionError("phase normalization left the reduced domain")
        reduced.append(gap)
        residue = (residue + gap) % 4
    return tuple(reduced)
