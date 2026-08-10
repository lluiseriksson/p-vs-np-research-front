# GATE-004U-BOUNDED-BLOCK-CONTEXTS — sparse neutral blocks force loss

**Label: NO-GO**

## Falsifiable theorem attempted

Attempted claim: exact SAT-gamma agreement on common-inner-length compact DNF
cores under every context in a neutral-padding family with at most `b(P)`
localized non-one blocks forces positive polynomial diagonal joint-quotient
loss in every minimum unrestricted circuit.

The attempted theorem is considered only in the quantitative regime

`m=floor(P/(b(P)+1))>=D(P)`,

where `D(P)` bounds block length. It is falsifiable by an agreeing total
function with nonpositive loss.

## Counterexample

LEMMA-049 constructs `m` disjoint clauses of width `b(P)+1`, each selecting
one coordinate from every segment of length `m`. A block of length at most
`D(P)<=m` hits at most one selected coordinate, and `b(P)` blocks cannot zero
all `b(P)+1` clause inputs. Their conjunction `W_P` is therefore one on every
required outer context.

Let `H(r,u)` be the polynomial-size total canonical DNF core evaluator with
distinct nonconstant diagonal residuals and `K=C(H)`. Then

`G(r,z,u)=H(r,u) AND W_P(z)`

agrees at every attempted-theorem witness. LEMMA-048/049 prove that the
displayed circuit is globally minimum, has exact size `K+(b+1)m`, quotient at
least `(b+2)m`, and loss at most `K-m`. Whenever `m>K`, the loss is negative.

Thus fixed-block-count forcing, and more generally every sparse-block regime
meeting the two quantitative inequalities, is false.

## Structural conclusion

Adding a fixed third, fourth, or any other fixed number of neutral blocks only
moves the counterexample to the next clause width. A viable context-only
defense must cross the quantitative boundary

`floor(P/(b(P)+1))<=max(D(P)-1,K(P))`,

or use witness interactions not representable as an isolated outer block
family. The next audit therefore uses unbounded block count and records its
growth explicitly; no fixed-width repair is pursued as if sufficient.

Full GATE-004U remains open because its complete DNF suffix set is not bounded
to a common core plus a sparse outer block family.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted circuits agreeing with exact SAT-gamma on common-inner-length DNF cores under sparse-block neutral contexts; exact diagonal semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform circuit adversary/base minimum circuit; uniform DNF maps and distant clause construction |
| Circuit size | Exact counterexample size `K+(b+1)m`; quotient at least `(b+2)m`; loss at most `K-m<0` when `m>K` |
| Circuit depth | Unrestricted base with width-`b+1` OR chains and a sequential AND tail |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Integer interval geometry only |
| Asymptotic quantifiers | Every parameter sequence with `m=floor(P/(b+1))>=D` and `m>K`; all compact DNF cores and qualifying sparse-block contexts |
| Regime | Worst-case exact counterexample to sparse-block context forcing; not a lower bound and not a counterexample to full GATE-004U |
