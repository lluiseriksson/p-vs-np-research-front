# LEMMA-045 — dense neutral padding blocks every raw-coordinate tail

**Label: PROVED**

## Statement

Fix any source string `phi` and padding length `P>=16` divisible by four. No
nonempty conjunction of literals on the first `P` raw coordinates is equal to
one on every member of the ENC-020 family `N_P(phi)`.

Consequently, LEMMA-044 cannot obtain even one fresh raw padding input, let
alone a growing tail, from agreement on every ENC-020 encoding of `phi`.

## Proof

Suppose a conjunction contains a literal on coordinate `i`. ENC-020 provides
one family member with bit zero at `i` and another with bit one. Therefore
neither the positive literal nor the negative literal is one throughout the
family. Any nonempty conjunction contains such a literal and fails on at least
one member. Only the empty conjunction is identically one. QED.

First equalize every compact DNF witness to a common inner length using
ENC-010, then apply this construction with the same outer budget to each
witness. This preserves each exact SAT output while varying every coordinate
in the common outer padding region. Any raw-coordinate face containing the
union of these witness families can fix coordinates only inside the common
inner region. If that region has length `O(RL)` and `P=Theta(n)`, the
`Theta(n)` outer fresh-tail mechanism in LEMMA-044 is eliminated.

## Scope

The lemma excludes only conjunctions of raw coordinate literals. The finite
witness family always has more complicated predicates that are one on all its
members, such as its membership predicate. Establishing an exact additive
minimum-cost tail from such a predicate would require a new theorem; LEMMA-037
does not apply because it requires genuinely fresh input variables.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact neutral SAT-gamma padding families and conjunctions of raw suffix-coordinate literals |
| Uniform/non-uniform | Uniform explicit witness family; arbitrary non-uniform raw-literal conjunction adversary |
| Circuit size | No lower bound; zero raw padding coordinates are available to a fresh-literal tail |
| Circuit depth | Unrestricted in later ambient circuits |
| Fan-in | Candidate raw tail uses AND two and optional NOT one; encoded contexts use standard formula fan-in |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean coordinate geometry only |
| Asymptotic quantifiers | Every source string and every padding length divisible by four and at least sixteen |
| Regime | Worst-case exact witness-location statement; does not prove GATE-004U or any circuit lower bound |
