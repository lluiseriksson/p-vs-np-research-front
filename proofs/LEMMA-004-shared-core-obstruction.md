# LEMMA-004 — maximal residual diversity can retain a shared core

**Label: PROVED**

## Statement

Let `S(h)` be minimum gate count for a Boolean function over fan-in-two
`AND/OR` and fan-in-one `NOT`, without free constant inputs. For every Boolean
function `G(u)` on `q>=1` inputs and every integer `p>=1`, define

`F(x,w,u) = G(u) XOR XOR_{i=1}^p (x_i AND w_i)`.

Then:

1. every `x_i` is essential for `F`;
2. the `2^p` restrictions `H_a(w,u)=F(a,w,u)` are pairwise distinct; and
3. for every `a`, `S(F)-S(H_a) <= 5p+3`.

Consequently, even a minimum circuit, essentiality of every restricted input,
and the maximum possible number of distinct residual functions do not imply a
superlinear-in-`p` circuit-size drop under restriction.

## Model card

| Field | Value |
|---|---|
| Computational model | General acyclic Boolean circuits over fan-in-two AND/OR and fan-in-one NOT |
| Uniform/non-uniform | Fully non-uniform circuit complexity |
| Circuit size | Exact minimum gate count; residual size gap at most `5p+3` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None; XOR is expanded into the Boolean basis |
| Asymptotic quantifiers | Every `p>=1`, every arity and function `G`, every restriction `a in {0,1}^p` |
| Regime | Worst-case exact total Boolean functions; no promise or distribution |

## Proof

Use the four-gate identity

`A XOR B = (A OR B) AND NOT(A AND B)`.

A minimum circuit for `G`, followed by `p` AND gates, `p-1` XORs for their
parity, and one final XOR with `G`, computes `F` using

`S(G)+p+4(p-1)+4 = S(G)+5p`

gates. Hence `S(F)<=S(G)+5p`.

For any fixed `a`, setting every `w_i=0` in `H_a` yields `G`. Restricting a
circuit may introduce Boolean constants. If the original basis has no free
constant inputs and at least one free input `u_1` exists, both constants can be
generated with at most three gates:

`not_u=NOT(u_1)`, `zero=AND(u_1,not_u)`, `one=NOT(zero)`.

Thus any circuit for `H_a` gives a circuit for `G` with at most three extra
gates, so `S(H_a)>=S(G)-3`. Combining inequalities gives

`S(F)-S(H_a) <= 5p+3`.

In particular, restricting any minimum circuit for `F` and normalizing it in
the same constant-free model cannot delete more than `5p+3` gates: the result
computes `H_a` and therefore has at least `S(H_a)` gates.

If `a` and `b` differ at coordinate `j`, choose `w_j=1`, all other `w_i=0`,
and any `u`. Then `H_a` and `H_b` have opposite values. Hence all `2^p`
residuals are distinct. The same assignment shows that flipping `x_j` changes
`F`, so every `x_j` is essential. QED.

## Scope

This is a generic shared-core obstruction, not a SAT lower bound. SAT-specific
syntax or semantics might force internal residual-gate collisions that this
construction avoids. The lemma proves that input essentiality and residual
function count—even at their maximum—cannot be the missing property by
themselves.
