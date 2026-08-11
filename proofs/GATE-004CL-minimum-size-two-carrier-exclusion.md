# GATE-004CL — exclude the two-gate carrier using the plateau budget

**Label: PROVED**

Assume a genuine extremal `W=1` plateau tuple whose canonical carrier is the
minimum case `H_{01,11}={h,n}` with `n=NOT h`. By LEMMA-190, `h` is deleted by
at least one of the three satisfying pruning maps, while `n` survives all
three because no NOT may be deleted.

## Falsifiable theorem

For every such tuple and pruning triple, at least one of the following holds.

1. Rewiring the surviving `n` after deletion of `h` supplies a LEMMA-183
   private-cone certificate or a same-size rewrite lowering an earlier
   extremal potential.
2. Preserving every `n`-to-output cancellation path requires at least two
   additional binary eliminations in that same satisfying code, exceeding
   the exact two-gate budget together with `h`.
3. The pruning deletes a non-bridge edge of the named cycle `gamma`, contrary
   to rank neutrality.
4. The three pruning maps and their symbolic cofactor identities are jointly
   unrealizable.

## Resolution

Alternative 4 always holds. LEMMA-192 proves that carrier canonicity would
force a direct raw-`u` input to `h`, while LEMMA-179 forbids that input in a
minimum plateau. Hence the size-two carrier is unrealizable under the full
minimum-plateau hypotheses. No rewiring or cycle argument is needed.

LEMMA-191 remains the necessary audit: it shows why minimum-plateau mixing,
not the two-vertex topology and output table alone, supplies the contradiction.

## Model card

| Field | Value |
|---|---|
| Computational model | Extremal minimum unrestricted switching plateau parent at `W=1` with carrier exactly `{h,n}` and three pruning maps |
| Uniform/non-uniform | Every individual finite non-uniform operational size-two-carrier tuple |
| Circuit size | Parent size `K+2`; each satisfying pruning deletes exactly two binary gates; proposed rewrites preserve size |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted and explicitly audited |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactor substitution and undirected cycle minors over `F_2` |
| Asymptotic quantifiers | Every nonconstant base, every hypothetical minimum size-two-carrier parent, and every valid satisfying pruning triple |
| Regime | Exact worst-case exclusion of the first bounded-carrier case; not exclusion of the plateau, a SAT lower bound, or terminal result |
