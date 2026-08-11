# Cycle 130 formula-excess exclusion audit

## Formula-excess theorem

**Label: PROVED**

LEMMA-159 proves that a read-once formula with `j+s` NOT gates can support a
base surplus of at most `s`. Hence the near-maximal premise `sigma>=2`
excludes the global one-extra-NOT formula. An exact formula residual can only
come from a parent with `N=j,r=1`.

## Cofactor boundary

**Label: NO-GO**

A gate that is `NOT u_i` under one satisfying base assignment may globally be
`NOT(u_i OR R(X))`. Residual private-NOT status alone does not prove parent
support or pruning. No minimum/unicyclic counterexample is claimed.

## Next attack

**Label: EXPLORATORY**

GATE-004BF isolates the unicyclic parent. Its proof must combine LEMMA-120's
one-bit factorization with the exact clause subtrees of the satisfying
cofactor and track all output paths under neutral restriction.

## Scope

**Label: EXPLORATORY**

No unicyclic resource-pruning theorem, full GATE-004BE, SAT lower bound, or
terminal result is claimed.
