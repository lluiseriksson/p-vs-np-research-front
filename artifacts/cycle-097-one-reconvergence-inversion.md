# Cycle 097 one-reconvergence inversion

## Structural result

**Label: PROVED**

LEMMA-110 proves that a circuit for the fixed-sign tail with one binary gate
above minimum connectivity has a unicyclic output graph. Unfolding that graph
into a formula copies every gate at most twice. Since the formula inversion
cost is `m`, the original circuit needs at least `ceil(m/2)` NOT gates; Markov
independently supplies `ceil(log_2(m+1))`.

## Quantitative method audit

**Label: NO-GO**

For the width-five specialization, the total lower certificate is
`5m+max(ceil(m/2),ceil(log_2(m+1)))`. It meets or exceeds the `6m-1` target
through `m=4`; from `m=5` its deficit is positive and tends to `m/2`. One-cycle
unfolding therefore does not close GATE-004AG. No smaller circuit, circuit
lower bound, or terminal result is claimed.
