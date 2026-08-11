# GATE-004BY — pair-minimality excludes an interleaved two-gate plateau

**Label: EXPLORATORY**

Let `A=J_{j-1}` and `F=A AND (t_j OR NOT u_j)` in an operational
GATE-004BX instance. For a circuit `C`, let `T_j(C)` count noninput gate
functions depending essentially on `u_j` or `t_j`. If `C(F)=C(A)+2`, choose
among all minimum parents one minimizing `T_j`.

## Falsifiable theorem

Every such hypothetical pair-minimal parent admits a function-preserving
same-size rewrite with strictly smaller `T_j`.

The theorem contradicts the defining minimality and therefore rules out the
two-gate increment. LEMMA-152 then forces the exact three-gate increment,
equivalently a one-unit rise of `N+r`. This supplies the one-step descent in
the vertical chain, bypassing the stronger restriction-local conclusion of
GATE-004BX.

LEMMA-178 gives the starting structure: `T_j>=3`; every satisfying code
produces a minimum circuit for `A`; no NOT or cycle coordinate is lost; and
at least one pair-sensitive gate survives as base computation in each code.
The missing exchange must uncross one such interleaved survivor. Disjoint
support or an output-only shell cannot supply it.

LEMMA-179 further localizes the interleaving: a `u_j`-sensitive NOT survives
all three satisfying codes, depends on the base, and receives an internal
mixed binary signal with no direct fresh-pair input. A literal `NOT u_j`
argument is `NO-GO`. GATE-004BZ is the active local uncrossing of this mixed
surviving NOT.

## Model card

| Field | Value |
|---|---|
| Computational model | Pair-sensitivity-minimal minimum unrestricted circuits at a hypothetical two-gate implication increment |
| Uniform/non-uniform | Extremal choice for every individual non-uniform operational prefix; uniform fresh implication pair |
| Circuit size | Hypothetical `C(F)=C(A)+2`; target contradiction forces exact increment three and one resource unit |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Four Boolean cofactors and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every operational GATE-004BX prefix and every pair-minimal minimum parent under the two-gate hypothesis |
| Regime | Exact worst-case sufficient interleaving-exclusion gate; not a SAT lower bound or terminal result |
