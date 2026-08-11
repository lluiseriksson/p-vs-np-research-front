# GATE-004BL — prune a resource from higher-rank one-excess parents

**Label: EXPLORATORY**

Assume `sigma>=2`, `Delta_j=sigma-1`, and let a minimum pruned circuit for
`J_j` have

`N+r=j+1`, `r>=2`.

## Falsifiable theorem

Prove that some neutral clause restriction leaves `N+r<=j`.

A compatible higher-rank minimum parent retaining all `j+1` resources under
every neutral clause restriction falsifies the theorem.

## Position in GATE-004BE

LEMMA-159 excludes rank zero. GATE-004BF, GATE-004BG, and GATE-004BI close
rank one. Thus GATE-004BL is exactly the remaining parent-rank range of the
one-excess pruning gate GATE-004BE.

LEMMA-158 constrains satisfying-base residuals to the higher-rank equality
line `q=m-rho+1` or to a lower-rank residual obtained by deleting parent
resources. The next attack must generalize the one-bit partition argument to
a bounded collection of cycle-source bits without losing the clause/resource
survival accounting.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum pruned unrestricted implication circuits with one resource excess and cycle rank at least two |
| Uniform/non-uniform | Every individual non-uniform higher-rank parent; uniform symmetric tail |
| Circuit size | Exact `N+r=j+1`, `r>=2`; target restricted `N+r<=j` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2` and Boolean restriction semantics |
| Asymptotic quantifiers | Every `j>=2`, `sigma>=2`, and higher-rank parent in the near-maximal descent range |
| Regime | Falsifiable worst-case remaining subgate of GATE-004BE; not a SAT lower bound or terminal result |
