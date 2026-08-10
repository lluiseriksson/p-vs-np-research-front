# GATE-004AQ — exclude the nested theta split

**Label: PROVED**

## Falsifiable theorem

Prove that no theta-core circuit with one binary core source, one downstream
non-source binary split, and exactly three NOT gates computes `W_6`.

No such circuit exists. By
LEMMA-129/130 this is the sole remaining orientation in GATE-004AP, hence in
GATE-004AO/AN.

## Proof

Apply LEMMA-131 with `m=6` and `q=3` to the first source bit. If its variable
partition cuts no clause, the lemma gives `q>=6`, contradiction. If it cuts
one clause, fixing the source to force that clause leaves a residual
formula/unicyclic `W_5` requiring `q-h>=5`, again impossible because `q=3`.

Thus the final nested theta orientation is empty.

## Scope

Together with LEMMA-128/130 this proves GATE-004AP and GATE-004AO; with
LEMMA-125/126 it proves GATE-004AN and the size-six Hall consequence
LEMMA-132. Size seven and every terminal bridge remain open.

## Model card

| Field | Value |
|---|---|
| Computational model | Nested-split theta-core bicyclic circuits for fixed `W_6` with exactly three NOT gates |
| Uniform/non-uniform | Every individual non-uniform final theta orientation |
| Circuit size | Excludes the final `c=2,q=3`, 31-binary-gate orientation stratum |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed theta topology and triangular Boolean interfaces |
| Asymptotic quantifiers | Fixed `W_6` and every nested theta candidate with three NOT gates |
| Regime | Exact finite structural exclusion; not full Hall, a SAT lower bound, or terminal result |
