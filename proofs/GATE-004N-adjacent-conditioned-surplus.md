# GATE-004N — adjacent conditioned-SAT surplus

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n_0` such that for
every `n>=n_0` and every minimum circuit `C_n` for `SAT-gamma_n`, set

`L=floor(c log_2 n)`

and use the identifier set `J_L^*` and the one-bit conditioned prefixes
`Q_{j,0},Q_{j,1}` from ENC-013. Let `P_n` be the number of parent gate labels
whose semantic functions depend on their common `6L+13`-bit prefix block.
For each `j`, define `z_j,t_j,kappa_j,lambda_j` using LEMMA-024 and LEMMA-029
for the adjacent prefix pair. Then

`sum_{j in J_L^*}(z_j-t_j+kappa_j+lambda_j)`

`>= |J_L^*|(B P_n^eta+1)`.

The theorem is falsified by any sufficiently large length and minimum SAT
circuit violating this inequality.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted SAT-gamma circuits and exact semantic joint quotients under adjacent complete prefix restrictions |
| Uniform/non-uniform | Fully non-uniform circuit adversary; uniform explicit adjacent-prefix family |
| Circuit size | Average collision-aware surplus at least `B P_n^eta+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed `0<c<1` and `B,eta>0`; every sufficiently large `n`; every minimum circuit; all `2^(L-2)` supported identifiers |
| Regime | Worst-case exact total-language computation; malformed strings reject; no promise or distribution |

## Bridge

ENC-013 supplies `|J_L^*|=2^(L-2)=Omega(n^c)` equal-length prefix pairs, each
differing in one bit, and their two conditioned residuals OR to exact SAT on
the suffix. The ENC-009 assignment witnesses restricted to `J_L^*`, together
with ENC-010 padding, still give all complementary columns at every sufficiently
large length. LEMMA-021 therefore gives `P_n>=|J_L^*|`.

LEMMA-029 and `alpha_j>=0` turn the displayed inequality into the required
average parent-to-joint-quotient loss. Adding one OR gate computes SAT on the
suffix of length `n-(6L+13)`. LEMMA-014 then yields a fixed superlinear
unrestricted SAT circuit lower bound, GATE-004.

## First attack boundary

The new fact is adjacency: after the other prefix coordinates are fixed, the
two residuals are opposite cofactors of one input bit. LEMMA-032 shows that
adjacency, complementary active cofactors, and global minimum size still do not
generically force superconstant loss: `s XOR G` retains an arbitrary hard core
and loses at most four gates. A proof of GATE-004N must exploit the simultaneous
SAT-specific family of polynomially many adjacent edges and its off-edge
semantics.
