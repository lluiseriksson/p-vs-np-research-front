# LEMMA-159 — formula NOT excess bounds the base surplus

**Label: PROVED**

Let `C` be a variable-read-once formula computing

`J_j=H AND AND_{i=1}^j(t_i OR NOT u_i)`

with `j+s` NOT gates, where `s>=0`. If `H` depends essentially on `h` inputs
and has circuit complexity `K`, then

`sigma=K-h+1<=s`.

Consequently, under the near-maximal premise `sigma>=2` and
`N+r=j+1`, a minimum parent circuit cannot have cycle rank zero. Moreover, if
a satisfying-base residual is the exact formula stratum `q=j,rho=0`, then
the parent has exactly `N=j,r=1`.

## Proof

Normalize `C` by pushing NOT gates to the leaves. The minterm/LCA argument of
LEMMA-157 is independent of the total NOT count: every implication pair is a
canonical two-leaf subtree, and its opposite input polarities force at least
one NOT strictly inside that pair subtree. The `j` pair subtrees are disjoint,
so at least `j` NOT gates are private tail gates.

Set every tail clause to its neutral value and prune. All private pair gates
disappear. The residual is a variable-read-once formula for `H` with at most
`s` NOT gates and exactly `h-1` binary gates. Therefore

`K<=h-1+s`,

which is equivalent to `sigma<=s`.

Now assume `sigma>=2` and a near-maximal minimum circuit has `N+r=j+1`. If
`r=0`, it is variable-read-once and has `j+1` NOT gates, so the theorem with
`s=1` gives `sigma<=1`, a contradiction. Thus `r>=1`.

Finally suppose a satisfying-base restriction leaves `q=j,rho=0`. Since
restriction creates no NOT gate, `N>=j`. Together with `N+r=j+1` and `r>=1`,
this forces `N=j,r=1`.

## Model card

| Field | Value |
|---|---|
| Computational model | Variable-read-once AND/OR/NOT formulas and minimum one-excess parent circuits |
| Uniform/non-uniform | Every individual non-uniform formula; uniform disjoint implication tail |
| Circuit size | `j+s` formula NOTs imply `K<=h-1+s`; near-maximal parents have `r>=1`; exact-formula residual forces `N=j,r=1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout one in the formula case and unrestricted in the parent consequence |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean unateness, minterm LCA geometry, and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `j>=1`, every `s>=0`, every nonconstant essential base, and every compatible formula; every near-maximal parent for the consequences |
| Regime | Exact worst-case formula-excess theorem and topology exclusion; not unicyclic pruning, a SAT lower bound, or a terminal result |
