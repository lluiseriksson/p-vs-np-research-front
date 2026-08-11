# LEMMA-144 — dependency Hall lifts to every satisfiable base-tail conjunction

**Label: PROVED**

Let `H(X)` be a nonconstant Boolean function depending essentially on `h`
inputs, with `C(H)=K`. Let `Y` be fresh and disjoint, and put

`F(X,Y)=H(X) AND W_m(Y)`.

Then every pruned unrestricted circuit for `F` satisfies

`C(F)>=h+(p+2)m-1`.

Together with LEMMA-107,

`C(F)>=max(K+(p+1)m, h+(p+2)m-1)`.

Hence the deficit from the displayed upper bound `U=K+(p+2)m` is at most

`U-C(F) <= min(m,K-h+1)`.

## Tail Hall proof

Fix any assignment `x*` with `H(x*)=1`, any spanning tree of the full output
cone, and define dependency-cone resources for the tail clauses exactly as in
GATE-004AL. For a tail-index set `I` of size `k`, fix `X=x*` and set every
tail clause outside `I` to true. Constant propagation and pruning leave a
`W_k` circuit.

The lifting argument of LEMMA-116 gives

`q+r <= |union_{i in I}P_i(T)|`,

where `q,r` are the residual NOT count and cycle rank. LEMMA-139 gives
`q+r>=k`. Therefore every tail dependency-cone Hall inequality holds even in
the joint parent circuit, and Hall yields `N+r>=m` for its total NOT count
`N` and cycle rank `r`.

The joint function has exactly `h+(p+1)m` essential inputs. Its binary count
is

`B=h+(p+1)m-1+r`.

Thus

`B+N>=h+(p+2)m-1`.

The combined bound follows from LEMMA-107. Since essential connectivity gives
`K>=h-1`, the surplus `sigma=K-h+1` is nonnegative. In the canonical regime
`K=o(P)` and `m=Theta(P)`, one has `sigma<=K=o(m)`, so the displayed circuit
is asymptotically near-minimum within `o(m)` gates. Exact additivity and
quotient survival do not follow.

## Model card

| Field | Value |
|---|---|
| Computational model | Pruned unrestricted circuits for an arbitrary satisfiable base conjoined with a fresh disjoint one-negative clause product |
| Uniform/non-uniform | Fully non-uniform base and circuit; uniform tail restriction and Hall matching |
| Circuit size | Lower `h+(p+2)m-1`; combined deficit at most `min(m,K-h+1)` from upper `K+(p+2)m` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Fundamental cycle bases over `F_2`, Boolean restrictions, and finite Hall matching |
| Asymptotic quantifiers | Every nonconstant `H`, every fixed `p>=1`, every `m>=1`, and every pruned circuit for `H AND W_m` |
| Regime | Exact worst-case base-tail size lower bound and canonical near-minimality; not exact additivity, quotient stability, a SAT lower bound, or a terminal result |
