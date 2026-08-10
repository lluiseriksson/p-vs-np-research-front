# GATE-004AQ — exclude the nested theta split

**Label: EXPLORATORY**

## Falsifiable theorem

Prove that no theta-core circuit with one binary core source, one downstream
non-source binary split, and exactly three NOT gates computes `W_6`.

One explicit circuit with these parameters falsifies the theorem. By
LEMMA-129/130 this is the sole remaining orientation in GATE-004AP, hence in
GATE-004AO/AN.

The source tree computes a bit `z_1`. The later split computes a sequential
state `z_2=H(z_1,X_2)` before using it on two downstream branches. The next
brick must classify cofactor partitions through this triangular two-stage
interface and allocate the three NOT gates across its source, middle, and
downstream formula regions.

## Model card

| Field | Value |
|---|---|
| Computational model | Nested-split theta-core bicyclic circuits for fixed `W_6` with exactly three NOT gates |
| Uniform/non-uniform | Every individual non-uniform final theta orientation |
| Circuit size | Target exclusion of the final `c=2,q=3`, 31-binary-gate orientation stratum |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Directed theta topology and triangular Boolean interfaces |
| Asymptotic quantifiers | Fixed `W_6` and every nested theta candidate with three NOT gates |
| Regime | Exact finite structural gate; not full Hall, a SAT lower bound, or terminal result |
