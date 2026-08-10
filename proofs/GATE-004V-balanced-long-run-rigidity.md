# GATE-004V — balanced long-run product rigidity

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<1`, `B,eta>0`, and `n_0` such that for
every `n>=n_0`, put `L=floor(c log_2 n)`, `R=2^(L-2)`, and use the ENC-016
expanded prefix cube of length `p=6L+13`.

Let `C_L` be the finite explicit family containing every complete-assignment
conjunction and every compact partial-assignment conjunction used for the
ENC-018 diagonal ternary columns, over the exact ENC-016 identifier set. Let
`s=floor((R-1)/8)` and let

`t_0(L)=12+max_{phi in C_L}|phi|`.

Put

`rho=floor((n-p-t_0(L))/(4s))`

and put

`Delta=n-p-t_0(L)-4rho s`, `t(L,n)=t_0(L)+Delta`.

Thus `0<=Delta<4s`; ENC-010 pads every core in `C_L` to the common inner
length `t(L,n)`.
For sufficiently large `n`, `rho>=7`. Let `E_{L,n}` contain every suffix
formed by:

1. padding a core in `C_L` to length `t(L,n)` with ENC-010; and
2. prefixing it by every `s`-slot product from LEMMA-052, with slot length
   `4rho`.

Attempted theorem: if a total function `G:{0,1}^n->{0,1}` agrees with exact
`SAT-gamma_n` on every row in the expanded prefix cube and every suffix in
`E_{L,n}`, then every minimum unrestricted circuit `C` for `G` satisfies

`sum_context (|C|-q_context) >= R(B R^eta+1)`.

The statement is falsifiable by any agreeing total-function family and one
minimum circuit violating the inequality.

## Terminal bridge

Exact `SAT-gamma_n` satisfies the premise. The conclusion is the GATE-004Q
loss bound, so ENC-013 and LEMMA-014 yield the first superlinear unrestricted
SAT circuit lower bound GATE-004. The downstream terminal gaps remain exactly
those already recorded in the vertical map; this gate is not itself a P versus
NP theorem.

## Why this is the next brick

LEMMA-052 proves that the family is coordinate-dense and lies outside every
currently proved raw-literal, sparse-block, and bounded-zero-run exact-tail
counterexample. The gate asks for actual positive rigidity rather than another
padding property. No escape from known counterexamples is treated as evidence
for its conclusion.

The first attack must classify low-complexity predicates common to the full
slot product and determine whether any admits an exact additive extension with
more quotient classes than parent gates.

ENC-028 and LEMMA-053 complete the first class: every disjoint common positive-
clause family has size at most `6s<K`, so LEMMA-048 cannot certify a negative
tail. The next attack is signed disjoint clauses, where NOT-gate cost and
possible complement sharing prevent an automatic additive identity, followed
by overlapping and non-clausal predicates.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted circuits for total functions agreeing with SAT-gamma on the expanded prefix cube at balanced long-run slot-product DNF suffixes; exact diagonal semantic joint quotients |
| Uniform/non-uniform | Fully non-uniform circuit adversary; uniform expanded rows, DNF cores, padding, slot family, and parameters |
| Circuit size | Average diagonal parent-to-joint-quotient loss at least `B R^eta+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Affine prefix/assignment geometry over `F_2`; suffix syntax and circuits are Boolean |
| Asymptotic quantifiers | Exists fixed sufficiently small `c>0,B,eta>0`; every sufficiently large `n`; every eligible total `G`; every minimum circuit; all expanded rows and balanced product witnesses |
| Regime | Worst-case exact agreement on an explicit total-language subset; no promise, average-case distribution, or surrogate terminal claim |
