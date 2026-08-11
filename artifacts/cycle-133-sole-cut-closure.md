# Cycle 133 sole-cut closure audit

## Upstream base exclusion

**Label: PROVED**

LEMMA-163 shows that an essential upstream base bit plus the upstream half of
the cut clause would create at least three residual functions, contradicting
factorization through one bit. Therefore the sole-cut upstream formula has no
base input.

## Unicyclic closure

**Label: PROVED**

Neutralizing the cut clause makes the duplicated bit constant and destroys
the unique cycle. GATE-004BI, GATE-004BG, and GATE-004BF are consequently
proved. The earlier large-margin theorem remains a separately valid route.

## Next attack

**Label: EXPLORATORY**

GATE-004BL isolates the exact remaining range `r>=2` of GATE-004BE. It needs
a multi-cycle analogue of the one-bit residual partition plus resource
survival.

## Scope

**Label: EXPLORATORY**

No higher-rank one-excess pruning, full GATE-004BE, SAT lower bound, or
terminal result is claimed.
