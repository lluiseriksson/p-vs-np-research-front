# Cycle 113 general rank-tradeoff audit

## Inductive theorem

**Label: PROVED**

LEMMA-139 proves `q>=m-max(r-1,0)` for either polarity of `W_m` at every
cycle rank. The induction separates a block-cut articulation from a
no-articulation core; in the latter, deleting a directed core source reduces
rank by at least one.

## Consequences

**Label: PROVED**

LEMMA-140 proves the exact standalone size `C(W_m)=(p+2)m-1`. LEMMA-141
proves dependency-cone Hall expansion for every subset and every spanning
tree. Therefore GATE-004AL, GATE-004AI, and GATE-004AH are proved. The fixed
rank-four GATE-004AS is also a corollary.

## Adversarial boundary

**Label: NO-GO**

The theorem does not imply `C(H AND W_m)=C(H)+C(W_m)+1` for an external base
`H`, and it does not prove that the displayed tail's diagonal semantic classes
survive replacement by a minimum circuit. Promoting GATE-004AG from the
standalone theorem would silently assume the missing direct sum.

## Scope

**Label: EXPLORATORY**

GATE-004AG/AE, unrestricted SAT circuit lower bounds, and P versus NP remain
open. No proof-assistant certification or independent mathematical
certification is claimed.

## Verification execution

**Label: EXPLORATORY**

`verification/audit.py` passed after manifest regeneration. The full unittest
discovery run was attempted once with a 120-second bound. All tests printed
before the cutoff passed, but the suite did not finish before timeout; it is
therefore not recorded as a passing full-suite run and was not relaunched on
Windows. No high-memory test process remained visible afterward.
