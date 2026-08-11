# GATE-004CA — exclude satisfying-signature cancellation

**Label: EXPLORATORY**

Assume the pair-minimal plateau and earliest mixed NOT `n` of GATE-004BZ.

## Falsifiable theorem

The satisfying signatures are stable:

`n_01=n_11`.

Equivalently, if `n_01!=n_11`, the first binary cancellation gate from
LEMMA-180 admits a function- and size-preserving rewrite that lowers `T_j`,
or a satisfying restriction loses one NOT/cycle resource.

Either outcome excludes the switching branch. The remaining stable branch
confines the chosen NOT's `u` dependence to the falsifying `t=0` slice and is
the next care-set problem; GATE-004CA alone does not exclude the plateau.

GATE-004BZ-COFACTOR-ORDER-ONLY shows that pointwise order and final cofactor
equality are insufficient. The proof must use minimality of all three
satisfying minors, exact preservation of `N+r`, or the fourth zero cofactor.

## Model card

| Field | Value |
|---|---|
| Computational model | Pair-minimal minimum plateau circuits with a first binary cancellation after an earliest mixed NOT |
| Uniform/non-uniform | Every individual non-uniform operational plateau parent; uniform fresh implication pair |
| Circuit size | Same-size pair-sensitivity descent or one-unit satisfying-code resource loss in the switching branch |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Ordered Boolean cofactors and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every operational GATE-004BZ parent whose earliest mixed NOT has distinct `01,11` signatures |
| Regime | Exact worst-case switching-branch subgate; not a SAT lower bound or terminal result |
