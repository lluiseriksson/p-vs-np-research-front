# LEMMA-211 — a basis-two boundary with an expendable input descends

**Label: PROVED**

Use the refined minimum endpoint and let `b` be a boundary counted by `R_0`,
with counterflow input `r`. Assume:

1. `r` is a gate whose only outgoing edge is `r -> b`;
2. the Boolean function computed by `b` has a constant-free AND/OR/NOT
   formula with exactly two gates over existing globally `u`-independent
   signals, and the formula can be associated so that its inner-gate function
   is independent of both fresh inputs `u,t`; and
3. every leaf signal of that formula is distinct from `r,b` and is not a
   descendant of either gate.

Then the parent is not the refined minimum endpoint. Reusing `r` for the
formula's inner gate and `b` for its outer gate gives a circuit of no larger
size with an earlier-potential decrease or strict `R_0` descent.

## Proof

Every two-gate formula has one inner gate `q` and one outer gate. Retarget the
physical vertex `r` to compute `q` from the corresponding independent leaf
signals. Retarget `b` to apply the outer operation to `r` and any remaining
independent leaf. The nondescendant hypotheses preserve acyclicity.

The new function at `b` equals its old function by hypothesis. Every outgoing
edge of `b` is retained, so a topological induction shows that every gate
strictly downstream of `b` retains its function. The old function at `r` is
lost, but condition 1 says no gate other than `b` consumed it. No new physical
gate is introduced; any predecessor made dead by the rewrite may be retained,
so size is unchanged, or deleted for an immediate minimum-size contradiction.

The new function at `r` is independent of both `u,t`, and every input used by
the new `b` is globally `u`-independent. Thus `r` cannot become a misaligned
common gate counted by `W`, and no new `u`-sensitive direct child of `h` is
created. All other gate functions are unchanged. The earlier potentials `W`
and `Q` therefore do not increase; if either decreases, the earlier
lexicographic extremality is contradicted.

If both stay equal, the retargeted `b` no longer consumes `h`: its displayed
formula uses only globally `u`-independent leaves and the independent inner
signal at `r`. Thus `b` leaves `R_0`. Because old `r` had no other consumer
and every other gate and edge is unchanged, no other direct `h`-boundary can
enter `R_0`. Therefore `R_0` strictly decreases, contradicting the refined
endpoint.

## Model card

| Field | Value |
|---|---|
| Computational model | Lexicographically refined minimum unrestricted constant-free AND/OR/NOT DAG with free wires |
| Uniform/non-uniform | Every finite non-uniform endpoint parent and every counted boundary satisfying the aligned-inner two-gate and expendable-input certificate |
| Circuit size | Two physical gates are repurposed; size does not increase and may strictly decrease after dead-gate deletion |
| Circuit depth | Unrestricted; nondescendant formula leaves guarantee acyclicity |
| Fan-in | AND/OR two; NOT one; `r` has fanout exactly one to `b`; all fanouts of `b` are retained |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean signal equality, basis distance two, and physical DAG rewiring |
| Asymptotic quantifiers | Every nonconstant base, hypothetical refined endpoint, counted boundary, and supplied two-gate certificate |
| Regime | Exact worst-case sufficient exchange theorem; not existence of the certificate, a SAT lower bound, or terminal result |
