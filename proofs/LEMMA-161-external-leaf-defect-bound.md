# LEMMA-161 — external leaves bound nonprivate clause NOTs

**Label: PROVED**

Let `T` be a fanout-one AND/OR/NOT formula containing every variable of a
`b`-clause implication product `W_b` exactly once, together with `L` other
leaf occurrences called external. Fix all external leaves to constants,
propagate constants, and prune. Suppose the residual computes `W_b` or its
complement and every tail variable remains essential.

Then at least `b-L` distinct clauses have a NOT gate whose entire original
descendant subtree contains only the two variables of that clause. In
particular, if `b>L`, neutralizing one such clause deletes a NOT occurrence
from `T`.

## Proof

The residual is variable-read-once in the `2b` tail variables. Normalize its
NOT polarities as in LEMMA-157. Minterm/LCA geometry makes each implication
pair a disjoint two-leaf canonical subtree. Opposite polarities force at least
one surviving original NOT gate on exactly one branch inside every pair
subtree. Choose one such gate `n_i` for each clause.

The chosen gates lie in pairwise disjoint residual subtrees, hence they are
pairwise incomparable in the original formula tree: restriction contracts or
deletes nodes but cannot reverse ancestry between two surviving gates.

Call `n_i` bad if its original descendant subtree contains an external leaf.
Because the chosen subtrees are disjoint, different bad gates contain
different external leaf occurrences. There are at most `L` bad gates.
Every other chosen gate has no external descendant. Its tail descendants are
the same before and after the external restriction, and the residual pair
subtree contains only its clause variables. Thus it is already private in
the original formula. At least `b-L` clauses are good.

## Model card

| Field | Value |
|---|---|
| Computational model | Fanout-one AND/OR/NOT formulas under constant restrictions of counted external leaf occurrences |
| Uniform/non-uniform | Every individual non-uniform formula with a uniform implication-tail variable set |
| Circuit size | At least `b-L` original clause-private NOT gates |
| Circuit depth | Unrestricted formula depth |
| Fan-in | AND/OR two; NOT one; fanout one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Formula-tree ancestry, Boolean cofactors, and minterm LCA geometry |
| Asymptotic quantifiers | Every `b>=1`, every `L>=0`, and every external restriction satisfying the residual premise |
| Regime | Exact worst-case defect bound; not a general circuit theorem, SAT lower bound, or terminal result |
