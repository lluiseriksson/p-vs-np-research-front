# Cycle 096 one-negative formula boundary

## Standalone lower bound

**Label: PROVED**

LEMMA-109 proves that the standalone four-positive/one-negative clause product
has size between `min(6m-1,5m+ceil(log_2(m+1)))` and `6m-1`. Its inversion
decrease parameter is exactly `m`; minimum binary connectivity forces a
formula, while one extra binary gate permits only the weaker circuit
inversion bound. The displayed circuit is exact for `m=1,2,3,4`.

## Asymptotic method audit

**Label: NO-GO**

From `m=5`, the certificate is short by
`m-1-ceil(log_2(m+1))`, a linear quantity. Connectivity plus inversion
complexity therefore cannot prove the asymptotic GATE-004AG minimality branch
and says nothing representation-independent about diagonal quotient classes.
GATE-004AG and GATE-004AE remain `EXPLORATORY`; no terminal progress follows.
