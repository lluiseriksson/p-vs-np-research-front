# GATE-004U-TWO-BLOCK-CONTEXT-ONLY — almost pairwise density forces loss

**Label: NO-GO**

## Falsifiable theorem attempted

Fix common-inner-length compact DNF cores and require exact SAT-gamma agreement
under every one/two-block ENC-022 outer context. Attempted claim: this almost
pairwise-zero syntax density forces positive polynomial average diagonal
joint-quotient loss in every minimum unrestricted circuit.

The theorem is falsifiable by an agreeing total function with a minimum
circuit whose average diagonal loss is nonpositive.

## Counterexample

For a twelve-divisible outer length `P>=84`, put `m=P/3` and define

`W_P(z)=AND_{i=0}^{m-1}(z_i OR z_{i+m} OR z_{i+2m})`.

Each ENC-022 context has at most two inserted blocks. Its zeros therefore lie
in at most two intervals of length at most 28. The three coordinates in every
clause are mutually separated by at least `m>=28`, so one block can zero at
most one coordinate and the two blocks can zero at most two. Hence `W_P=1`
on the entire ENC-022 family.

Let `H(r,u)` be the polynomial-size total canonical DNF core evaluator used in
the preceding syntax no-go audits, with distinct nonconstant diagonal
residuals, and set

`G(r,z,u)=H(r,u) AND W_P(z)`.

This agrees at every witness in the attempted theorem. LEMMA-048 proves exact
parent size `K+P`, at least `4P/3` quotient classes per diagonal pair, and
loss at most `K-P/3`. Choosing the fixed context exponent small enough gives
`K=o(P)`, so the loss is negative at infinitely many compatible lengths.
The attempted theorem is false.

## Structural conclusion

Pairwise zero coverage blocks width-two clauses but cannot block width-three
clauses when every required context contains at most two localized non-one
blocks. Any next neutral-context defense must allow at least three blocks and
supply triple-zero coverage, or use the broader DNF syntax set to invalidate
the common predicate. Even triple coverage would address only width three;
LEMMA-048 applies at every fixed width.

Full GATE-004U remains open because its complete suffix set is broader than
the common-inner-length ENC-022 family isolated here.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits agreeing with exact SAT-gamma on common-inner-length DNF cores under every ENC-022 context; exact diagonal joint quotients |
| Uniform/non-uniform | Fully non-uniform circuit adversary and base minimum circuit; uniform DNF maps, two-block contexts, and distant triples |
| Circuit size | Counterexample exact size `K+P`; quotient at least `4P/3`; loss at most `K-P/3<0` asymptotically |
| Circuit depth | Unrestricted base with width-three OR chains and a sequential AND tail |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Infinitely many compatible lengths with twelve-divisible `P>=84`, every compact DNF core and ENC-022 placement, and sufficiently small fixed context exponent `c` |
| Regime | Worst-case exact counterexample to ENC-022-only forcing; not a lower bound and not a counterexample to full GATE-004U |
