# Cycle 114 base-tail bottleneck audit

## Enabled tail

**Label: PROVED**

LEMMA-142 proves `C(z AND W_m)=(p+2)m` and
`C(NOT z AND W_m)=(p+2)m+1`. The second code uses LEMMA-140's heterogeneous
one-negative-clause corollary, preventing an invalid assumption that
complementing the base output preserves its size exactly.

## Bottleneck implication

**Label: CONDITIONAL**

LEMMA-143 proves that a pure-base one-vertex separator in a minimum circuit
would split the gate budget into at least `K` upstream and `(p+2)m`
downstream, closing alternative 1 of GATE-004AG.

## Failed existence argument

**Label: NO-GO**

Fresh disjoint supports alone do not force an unrestricted circuit DAG to
contain that separator. GATE-004AT remains `EXPLORATORY`; the next attack must
use canonical agreement rows or a size-nonincreasing uncrossing theorem.

## Scope

**Label: EXPLORATORY**

No base-tail additivity, SAT circuit lower bound, or terminal result is
claimed. The real-progress estimate remains zero.
