# GATE-004AG-CYCLE-RANK-UNFOLDING-ONLY — cycle-rank unfolding proves minimality

**Label: NO-GO**

LEMMA-111 exhausts the direct cycle-rank unfolding method over every binary-
gate count. If the output-cone cycle rank is `t`, unfolding copies any NOT at
most `2^t` times and yields

`N>=max(ceil(m/2^t),ceil(log_2(m+1)))`.

After charging the `t` extra binary gates and optimizing, the method proves
only

`C(W_m)>=5m-1+g(m)`,

where

`g(m)=min_{t>=0}[t+max(ceil(m/2^t),ceil(log_2(m+1)))]`.

But `g(m)=Theta(log m)`, while the displayed `6m-1` circuit requires a
surplus `m`. The method therefore leaves deficit
`m-g(m)=m-Theta(log m)`. This is positive from `m=5` and linear.

The failure is structural: cycle rank bounds the number of unfolding copies,
but optimizing the cost of reconvergence against copied negations permits a
logarithmic certificate only. Improving the desired lower bound requires
function-specific restrictions on how reconvergences can share the negative
variables, or a direct semantic quotient theorem over the canonical base.

This is a method no-go. It provides no smaller circuit and does not refute
GATE-004AG, GATE-004AE, an unrestricted SAT circuit lower bound, or P versus
NP.

## Model card

| Field | Value |
|---|---|
| Computational model | All pruned unrestricted Boolean circuit output cones, binary cycle-rank unfolding, and inversion complexity |
| Uniform/non-uniform | Every individual non-uniform circuit; uniform fixed-sign tail family |
| Circuit size | Lower `5m-1+g(m)` versus target `6m-1`, with deficit `m-g(m)=m-Theta(log m)` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected binary cycle space over `F_2` and Boolean-lattice inversion |
| Asymptotic quantifiers | Every `m>=1`, every cycle rank `t>=0`, and every pruned circuit in the corresponding binary-gate stratum |
| Regime | Structural no-go for cycle-rank unfolding as a complete method; larger gates remain open |
