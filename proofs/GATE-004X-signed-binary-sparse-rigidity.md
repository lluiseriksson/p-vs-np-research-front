# GATE-004X — rigidity under implication-sparse long-run slot products

**Label: EXPLORATORY**

## Falsifiable theorem

Use the exact GATE-004V expanded prefix rows and compact DNF core family, but
put

`s=floor((R-1)/24)`

and replace each balanced slot option set by `S^+_rho` from LEMMA-060. Define
`rho`, the common inner padding length, and the total length exactly as in
GATE-004V with this value of `s`; for every sufficiently large `n`,
`rho>=13`.

Claim: there exist fixed constants `0<c<1`, `B,eta>0`, and `n_0` such that
for every `n>=n_0`, every total function agreeing with exact `SAT-gamma_n` on
the complete expanded-row/enhanced-slot witness set, and every minimum
unrestricted circuit `C` for that function,

`sum_context (|C|-q_context) >= R(B R^eta+1)`.

All contexts, rows, quotient definitions, and asymptotic quantifiers not
changed above are exactly those of GATE-004V. Any agreeing total-function
family with one minimum circuit violating the inequality falsifies the gate.

## Terminal bridge

Exact `SAT-gamma_n` agrees on the enhanced witness set. The conclusion is the
same GATE-004Q diagonal loss bound, so the already proved ENC-013/LEMMA-014
recurrence bridge yields GATE-004, the first superlinear unrestricted SAT
circuit lower bound. GATE-005 and the remaining terminal amplification are
still open; GATE-004X is not a P-versus-NP theorem.

## Why this replaces GATE-004V as the smallest positive brick

GATE-004V retains `Theta(P)` disjoint common mixed implications. Their exact
circuit effect is the unresolved adversarial GATE-004W. LEMMA-060 enlarges
the witness family while preserving exact syntax, coordinate density, the
tunable long run, and the all-long packing witness. At the adjusted slot
count, every established disjoint positive or signed-binary tail is below the
unavoidable base floor.

This only removes a known binary vulnerability. It does not establish
positive loss. LEMMA-061 completes the first width-three incidence audit and
finds `rho*s=P/4` disjoint common signed triples. LEMMA-062 cannot yet turn
them into a minimum-circuit counterexample: its exact restriction certificate
is `2m` gates below the displayed circuit. GATE-004Y is now the active
falsification audit. Overlapping and nonclausal predicates remain unclassified.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for total functions agreeing with SAT-gamma on expanded rows and enhanced implication-sparse slot-product DNF suffixes; exact diagonal semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform circuit adversary; uniform rows, core family, fixed and tunable neutral blocks, placements, slots, and parameters |
| Circuit size | Average diagonal loss target at least `B R^eta+1`; eligible base floor `K>=R-1`; known disjoint signed-binary packing at most `18s<=3(R-1)/4` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine prefix/assignment geometry over `F_2`; suffix syntax and circuits Boolean |
| Asymptotic quantifiers | Exists fixed sufficiently small `c>0` and `B,eta>0`; every sufficiently large `n`; every agreeing total function; every minimum circuit; all enhanced witnesses |
| Regime | Worst-case exact agreement on an explicit total-language subset; no promise, distributional, average-case, or surrogate terminal claim |
