# Cycle 159 — minimum carrier exclusion audit

**Label: PROVED**

LEMMA-192 excludes `|H_{01,11}|=2` in every genuine minimum two-gate plateau
switching branch. Canonicity forces a carrier path from the only differing raw
source `u` to `h`; a two-gate carrier would make `u` a direct input of `h`,
contradicting the mixed-surviving-NOT theorem LEMMA-179.

Combined with LEMMA-190, the conditional `W=1` carrier range is now exactly
bounded by `3<=|H|<=7`. This does not show that `W=1` is reached or exclude
any carrier in the remaining range.

## Classification

- LEMMA-192: `PROVED`
- GATE-004CL: `PROVED`
- GATE-004CM: `EXPLORATORY`
- P versus NP: unresolved
