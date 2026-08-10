# GATE-004Z-STANDALONE-SEPARATE — signed triples provide an independent size route

**Label: NO-GO**

## Rejected route

Treat the standalone factorized signed-triple size problem, or its displayed
minimality over a disjoint base, as a structurally new route that may avoid
the unresolved implication-tail bottleneck.

## Failure

LEMMA-066 proves the exact identity

`C(H AND AND_i[p_i OR NOT(u_i AND v_i)])`

`= C(H AND AND_i[p_i OR NOT t_i]) + m`.

The upper direction inserts the `m` pairwise-AND gates; the lower direction
restricts one input of each pair to one and deletes at least `m` gates. A
minimum implication circuit therefore lifts to a minimum signed-triple
circuit, with the `m` derived-input gates adding exactly `m` quotient classes.

Consequently factorized signed-triple minimality is equivalent to the
corresponding implication-tail minimality plus a settled additive term. It is
not an independent escape from GATE-004W. This does not resolve the implication
gate or the representation-independent alternative in GATE-004Z.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted Boolean circuits, disjoint implication tails, derived pairwise-AND substitution, restrictions, and semantic quotients |
| Uniform/non-uniform | Fully non-uniform bases and minimizing circuits; uniform exact reduction |
| Circuit size | Exact additive identity `C(F)=C(J)+m`; no lower bound beyond the unresolved implication component |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; Boolean functional substitution only |
| Asymptotic quantifiers | Every finite nonconstant disjoint base and every `m>=1` |
| Regime | Structural route no-go only; implication minimality, quotient survival, GATE-004Z, GATE-004X, and P versus NP remain open |
