# GATE-004AG-ONE-CYCLE-UNFOLDING-ONLY — one-cycle unfolding closes the tail

**Label: NO-GO**

LEMMA-110 strengthens the first non-formula boundary. With exactly `5m`
binary gates, the output graph is unicyclic, circuit unfolding duplicates
each NOT at most twice, and formula inversion gives `N>=ceil(m/2)`. Combined
with Markov, the exact certificate is

`N >= max(ceil(m/2),ceil(log_2(m+1)))`.

The displayed target size is `6m-1`. Even on this single-reconvergence
stratum, the resulting total-size certificate is short by

`m-1-max(ceil(m/2),ceil(log_2(m+1)))`,

which is positive from `m=5` and asymptotic to `m/2`. Formula unfolding alone
cannot recover which duplicated NOT copies should be charged to the same
original gate, so its factor-two loss is exactly where the proof stops.

This is a method no-go, not a smaller-circuit construction. It neither
refutes the stronger negation tradeoff, GATE-004AG, or GATE-004AE nor proves
an unrestricted SAT lower bound or P versus NP. The next gate is the general
cycle-rank tradeoff: quantify how `t` independent reconvergences can reduce
formula inversion cost before the additional binary gates themselves close
the size bound.

## Model card

| Field | Value |
|---|---|
| Computational model | Unicyclic unrestricted Boolean circuit output cones, formula unfolding, and inversion complexity |
| Uniform/non-uniform | Every individual non-uniform circuit in the exact one-extra-binary stratum |
| Circuit size | Lower `5m+max(ceil(m/2),ceil(log2(m+1)))` versus target `6m-1`; asymptotic deficit about `m/2` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected multigraph cycle rank and Boolean-lattice inversion only |
| Asymptotic quantifiers | Every `m>=1` and every pruned circuit in the exactly `5m`-binary-gate stratum |
| Regime | Structural no-go for one-cycle unfolding as a complete proof method; larger gates remain open |
