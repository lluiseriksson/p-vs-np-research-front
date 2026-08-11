# LEMMA-157 — every read-once implication block consumes a private NOT

**Label: PROVED**

Let `H` be nonconstant and depend essentially on `h` inputs. Suppose a
variable-read-once AND/OR/NOT formula `C` computes

`J_j=H AND AND_{i=1}^j(t_i OR NOT u_i)`

and contains exactly `j` NOT gates. Then:

1. each implication pair `{u_i,t_i}` contains exactly one private NOT, on
   the `u_i` branch;
2. there are no NOT gates outside those `j` pair subtrees;
3. neutralizing any pair by `(u_i,t_i)=(0,1)` prunes its private NOT and
   leaves a formula for `J_{j-1}` with exactly `j-1` NOT gates; and
4. `H` has a monotone read-once formula, so `C(H)=h-1` and `sigma=0`.

Consequently a positive maximal deficit `Delta_m=sigma>0` cannot occur.

## Normalize the read-once tree

Push every internal NOT toward the leaves using De Morgan's laws and cancel
double negations. This changes gate labels but does not duplicate any
variable or change the underlying binary branching tree. A function computed
by a variable-read-once formula is unate: the polarity of each essential
variable is the parity of the NOT gates on its unique leaf-to-root path.

Complement every negative-polarity input variable and call the resulting
positive variables `z`. The normalized tree is a monotone read-once formula
for

`J_j^+=H^+(z) AND AND_{i=1}^j(a_i OR t_i)`,

where `a_i=NOT u_i` is now treated as a positive variable and `H^+` is
monotone. This normalization is the special unate case of the read-once
framework recorded in KLNSW93.

## Each implication pair is a canonical subtree

For a monotone function, join two variables by an edge when some minterm
contains both. In a monotone read-once tree, two leaves are adjacent exactly
when their lowest common ancestor is an AND gate: a minimal true assignment
to an AND combines minterms from both children, whereas a minterm of an OR
uses only one child.

For fixed `i`, no minterm of `J_j^+` contains both `a_i` and `t_i`, because
either one minimally satisfies their OR clause. On the other hand, every
essential variable outside this pair co-occurs in a minterm with `a_i` and
also with `t_i`: take a minterm of its own disjoint factor and one minimal
choice from every other factor.

Let `v_i` be the LCA of `a_i,t_i`. It is therefore an OR gate. If an outside
leaf lay below `v_i`, its LCA with at least one of `a_i,t_i` would also be
that OR gate, contradicting the two required co-occurrence edges. Hence the
subtree of `v_i` contains exactly the pair. These `j` pair subtrees are
pairwise disjoint.

## Count the private polarities

Return to the original formula. The root paths of `u_i` and `t_i` coincide
above their pair LCA. Their output polarities are opposite, so the parity of
NOT gates on the two branches strictly below that LCA differs. At least one
NOT gate is therefore private to that pair subtree. Disjointness of the pair
subtrees gives at least `j` distinct NOT gates.

The formula has exactly `j`, so equality leaves exactly one private NOT in
each pair and none anywhere else. With no common or external NOT, the
negative variable `u_i` has the unique NOT and the positive variable `t_i`
has none. Setting `(u_i,t_i)=(0,1)` makes the pair subtree constant one;
constant propagation deletes its private NOT and leaves exactly `j-1` NOT
gates.

Finally set every tail clause to one. No NOT remains, and pruning leaves a
monotone read-once formula for `H`. It has `h-1` binary gates, so
`K<=h-1`. Essential-input connectivity gives `K>=h-1`; hence `K=h-1` and
`sigma=K-h+1=0`.

## Model card

| Field | Value |
|---|---|
| Computational model | Variable-read-once AND/OR/NOT formulas, De Morgan normalization, and monotone minterm co-occurrence trees |
| Uniform/non-uniform | Every individual non-uniform read-once formula for the uniform disjoint implication family |
| Circuit size | Exactly one private NOT per implication pair; exact base complexity `h-1`; positive maximal deficit excluded |
| Circuit depth | Unrestricted read-once formula depth |
| Fan-in | AND/OR two; NOT one; fanout one in the output cone |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean unateness, minterms, and tree LCA only |
| Asymptotic quantifiers | Every `j>=1`, every nonconstant essential base `H`, and every variable-read-once formula with exactly `j` NOT gates computing `J_j` |
| Regime | Exact worst-case equality-stratum theorem; not intermediate-deficit localization, a SAT lower bound, or a terminal result |
