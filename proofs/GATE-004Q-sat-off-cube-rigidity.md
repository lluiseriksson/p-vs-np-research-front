# GATE-004Q — SAT off-cube rigidity for adjacent conditioned quotients

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n_0` such that for
every `n>=n_0` and every minimum circuit `C_n` for the full total function
`SAT-gamma_n`, set `L=floor(c log_2 n)`, `R=2^(L-2)`, and use all ENC-014
adjacent conditioned pairs. If `q_s` is the exact semantic joint quotient size
for context `s`, then

`sum_{s in {0,1}^{L-2}} (|C_n|-q_s) >= R(B R^eta+1)`.

Unlike GATE-004P, this theorem is explicitly about the ambient SAT function on
every prefix string, not about an abstract function constrained only on the
embedded cube and its witnesses.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for the exact total SAT-gamma language and exact semantic quotients under ENC-014 adjacent complete prefix restrictions |
| Uniform/non-uniform | Fully non-uniform minimum-circuit adversary; uniform explicit restriction family |
| Circuit size | Average parent-to-joint-quotient loss at least `B R^eta+1`, where `R=2^(L-2)` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; ENC-014's affine geometry only parametrizes Boolean input rows |
| Asymptotic quantifiers | Exists fixed `0<c<1` and `B,eta>0`; every sufficiently large `n`; every minimum SAT-gamma circuit; all contexts |
| Regime | Worst-case exact total-language computation; malformed strings reject; no promise or distribution |

## Bridge

Each pair's two outputs OR to exact SAT-gamma on the suffix by ENC-013. The
length decreases by `6L+13=O(log n)`, while `R=Omega(n^c)`. Therefore the
displayed bound and LEMMA-014 give the fixed superlinear unrestricted SAT
circuit lower bound GATE-004.

## First attack boundary

LEMMA-038 proves that every abstract on-cube hypothesis audited so far is
insufficient, even with ambient minimality. ENC-015 now classifies the entire
one-bit off-cube halo. All six neighbors are valid formulas: two duplicate a
base residual, one is neighboring negative conditioning, one is the exact
union `H_{j,0} OR H_{j',0}`, and two are unions involving a positive
condition and an auxiliary negative condition.

LEMMA-039 and NG-037 show that the neutral duplicates alone force no circuit
structure, even under global minimality. LEMMA-040 then realizes all six
pointwise ENC-015 relations simultaneously in one total function while
retaining the fresh-tail quotient expansion. Thus the complete radius-one
relation schema is also `NO-GO` as a generic forcing principle.

GATE-004R is the next attack. It requires exact agreement with SAT-gamma on
the entire radius-two prefix cylinder, rather than a lookup function copying
only the simplified pointwise halo table. The first task is to classify all
two-flip rows, their cross-context collisions, and their exact total-language
semantics. Any forcing inference must identify a proved compatibility absent
from LEMMA-040.
