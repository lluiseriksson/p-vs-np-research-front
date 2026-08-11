# GATE-004AU — near-minimum canonical tails retain linear diagonal quotient

**Label: EXPLORATORY**

## Falsifiable theorem

For the canonical `p=4` base-tail function in GATE-004AG, write

`U=K+6m`, `S=C(F)`, and `Delta=U-S`.

Prove that some minimum circuit has diagonal quotient contribution from
tail-dependent gates at least

`7m-2(Delta+K)`.

Here the contribution is the number of distinct active nonconstant Boolean
functions obtained by restricting tail-dependent gates separately to the two
designated base rows, after discarding every class already realized by a
base-only gate. This is the same class-count convention used in LEMMA-107.

One canonical family for which every minimum circuit has a smaller tail
contribution falsifies the theorem.

## Bridge

LEMMA-144 gives `0<=Delta<=K-h+1<=K=o(m)`. If the theorem holds, the signed
parent-to-quotient loss is at most

`S-[7m-2(Delta+K)] <= 3K-m+Delta <=4K-m`,

which is negative for all sufficiently large canonical parameters. This
would close the width-five obstruction required by GATE-004AE without first
proving exact base-tail additivity or a topological bottleneck.

The coefficient two is explicit and part of the falsifiable claim; any proved
constant-coefficient stability bound strong enough to keep the error `o(m)`
would serve the same asymptotic bridge but must be recorded as a separate
theorem.

GATE-004AU-GLOBAL-SIZE-ONLY records why LEMMA-144 alone does not prove this:
global gate functions can become equal or inactive after the two diagonal row
restrictions. The next attack must charge each such row-cofactor collision to
the `Delta+K` slack budget or exploit canonical suffix dependence.

## Model card

| Field | Value |
|---|---|
| Computational model | Globally minimum unrestricted canonical base-tail circuits and two-row semantic diagonal quotients |
| Uniform/non-uniform | Uniform canonical rows and tail; fully non-uniform minimum-circuit adversary |
| Circuit size | Parent `S=K+6m-Delta` with `0<=Delta<=K`; target tail quotient at least `7m-2(Delta+K)` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean row cofactors and semantic equivalence classes; inherited affine row geometry only |
| Asymptotic quantifiers | Every sufficiently large compatible canonical parameter choice and some minimum circuit for each instance |
| Regime | Exact quantitative quotient-stability gate; not a SAT circuit lower bound or terminal result |
