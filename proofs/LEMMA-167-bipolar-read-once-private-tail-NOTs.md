# LEMMA-167 — exact bipolar read-once tails have private NOTs

**Label: PROVED**

Let `B` be a nonzero Boolean function on variables disjoint from `a`
implication pairs, and put

`P=B AND AND_{i=1}^a(t_i OR NOT u_i)`.

If a variable-read-once AND/OR/NOT formula computes either `P` or `NOT P`
with exactly `a` NOT gates, then every implication pair has exactly one NOT
gate private to its two-leaf subtree and there is no NOT outside those
subtrees. Neutralizing any pair by `(u_i,t_i)=(0,1)` prunes its private NOT.

The statement includes `B=1`.

## Proof

Every function computed by a variable-read-once formula is unate. Normalize
the formula by complementing input variables according to their output
polarity and pushing path parities into those renamed inputs. The underlying
binary read-once tree is unchanged.

For output `P`, the normalized monotone function has the form

`B^+ AND AND_i(alpha_i OR t_i)`.

The minterm co-occurrence argument of LEMMA-157 shows that the LCA of
`alpha_i,t_i` is an OR and that no outside leaf lies below it. Hence every
pair is an exact two-leaf OR subtree.

For output `NOT P`, reverse all essential polarities. The normalized monotone
function has the form

`B^- OR OR_i(u_i AND beta_i)`.

Now `u_i,beta_i` co-occur in a minterm, while no outside variable co-occurs
with either one. Their LCA is therefore an AND, and an outside leaf below it
would co-occur with one member of the pair. Thus every pair is an exact
two-leaf AND subtree.

In the original variables `u_i` and `t_i` have opposite polarities for either
selected output. Their paths coincide above the pair LCA, so their NOT
parities below that LCA differ. Each disjoint pair subtree therefore contains
at least one NOT. Exactly `a` NOTs force one per pair and none elsewhere.

Under `(u_i,t_i)=(0,1)`, the positive-polarity OR pair becomes one and the
negative-polarity AND pair becomes zero. Constant propagation deletes the
whole pair subtree, including its private NOT.

## Model card

| Field | Value |
|---|---|
| Computational model | Variable-read-once AND/OR/NOT formulas for either polarity of a base times disjoint implication clauses |
| Uniform/non-uniform | Every individual non-uniform formula; uniform symmetric tail family |
| Circuit size | Exactly `a` NOTs imply one private NOT per pair and none elsewhere |
| Circuit depth | Unrestricted read-once depth |
| Fan-in | AND/OR two; NOT one; fanout one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean unateness, minterms, and tree LCAs only |
| Asymptotic quantifiers | Every `a>=1`, every nonzero disjoint base `B`, and either output polarity |
| Regime | Exact worst-case bipolar formula theorem; not an unrestricted-circuit, SAT-lower-bound, or terminal result |
