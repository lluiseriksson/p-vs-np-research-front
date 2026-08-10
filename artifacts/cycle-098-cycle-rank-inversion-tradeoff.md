# Cycle 098 cycle-rank inversion tradeoff

## All-DAG lower bound

**Label: PROVED**

LEMMA-111 proves that cycle rank `t` permits at most `2^t` unfolding copies
of any gate. Formula inversion and Markov therefore give
`N>=max(ceil(m/2^t),ceil(log_2(m+1)))`. Optimizing over every binary-gate
count yields the exact method bound

`C(W_m)>=5m-1+g(m)`.

The optimization proves `g(m)=m` for `m<=4` and `g(m)=Theta(log m)`
asymptotically.

## Method outcome

**Label: NO-GO**

The target displayed circuit has size `6m-1`, so cycle-rank unfolding leaves
deficit `m-g(m)=m-Theta(log m)`, positive from `m=5`. This closes the entire
unfolding route quantitatively but neither constructs a smaller circuit nor
settles GATE-004AG. A function-specific reconvergence or direct quotient
theorem is still required; no circuit-lower-bound or terminal claim follows.
