# GATE-004BX — exploit all three satisfying implication codes

**Label: EXPLORATORY**

Assume a selector-minimal minimum representation from GATE-004BW computing

`H(x,Z) AND AND_i(t_i OR NOT u_i)`.

## Falsifiable theorem

There are an index `i` and a pair

`(a,b) in {(0,0),(0,1),(1,1)}`

such that restricting `(u_i,t_i)=(a,b)` with `x` free deletes a NOT from the
pruned output cone or lowers its undirected cycle rank.

Every displayed pair satisfies `t_i OR NOT u_i`, so the restriction computes
the same `(j-1)`-clause target. The claimed loss is therefore sufficient for
the one-step two-excess descent even though it allows two neutral codes beyond
the canonical `(0,1)` used in GATE-004BW.

## First audit

The four cofactor codes of one pair are respectively the same target at
`00`, `01`, and `11`, and zero at `10`. LEMMA-177 shows that selector
extremality without this three-equal/one-zero table cannot prove loss. If all
three satisfying restrictions preserve resources, LEMMA-174 identifies their
surviving cycle spaces, but an additional directed-path or gate-function
argument is required to make the fourth code incompatible with minimum `S`.

LEMMA-178 now proves the exact equality structure: failure through a
two-gate increment makes all three satisfying minors minimum and forces pair
dependence to survive as base computation. An exposed two-gate shell is
`NO-GO`; GATE-004BY is the active pair-minimal interleaving gate.

## Model card

| Field | Value |
|---|---|
| Computational model | Selector-minimal minimum unrestricted two-excess circuits for a disjoint implication product |
| Uniform/non-uniform | Every individual non-uniform remaining parent; uniform symmetric implication tail |
| Circuit size | Minimum parent resource `N+r=j+2`; target after one satisfying pair restriction at most `j+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four Boolean pair cofactors and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every operational GATE-004BW instance and all three satisfying codes of every implication pair |
| Regime | Exact worst-case sufficient weakening of the canonical-neutral gate; not a SAT lower bound or terminal result |
