# GATE-004BF — prune one resource from the unicyclic parent

**Label: EXPLORATORY**

Assume `sigma>=2`, `Delta_j=sigma-1`, and let a minimum pruned circuit `C`
for `J_j` have

`N=j`, `r=1`.

## Falsifiable theorem

Prove that some clause-neutral restriction `(u_i,t_i)=(0,1)` leaves a circuit
for `J_{j-1}` with

`N+r<=j`.

A compatible unicyclic minimum parent retaining all `j+1` resources under
every neutral clause restriction falsifies the theorem.

## Position in the active gate

LEMMA-159 excludes the global formula `N=j+1,r=0`. It also shows that every
parent whose satisfying-base residual is the exact `j`-NOT formula lies in
this unicyclic stratum. Thus GATE-004BF closes the first and most rigid branch
of LEMMA-158 and is a genuine subgate of GATE-004BE.

LEMMA-120 factors the unique cycle through one upstream formula bit. The next
proof obligation is to combine that factorization with the canonical private
NOT subtrees seen after a satisfying-base restriction, while tracking whether
neutralizing a clause deletes a NOT or breaks the unique cycle.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unicyclic AND/OR/NOT circuits for base conjoined with disjoint implication clauses |
| Uniform/non-uniform | Every individual non-uniform unicyclic minimum parent; symmetric uniform clause family |
| Circuit size | Exact parent `N=j,r=1`; target restricted `N+r<=j` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted with one undirected cycle |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | One-bit Boolean factorization and undirected cycle rank over `F_2` |
| Asymptotic quantifiers | Every `j>=2` in the near-maximal unicyclic parent stratum with `sigma>=2` |
| Regime | Falsifiable worst-case subgate of GATE-004BE; not full GATE-004BD/BA, a SAT lower bound, or a terminal result |
