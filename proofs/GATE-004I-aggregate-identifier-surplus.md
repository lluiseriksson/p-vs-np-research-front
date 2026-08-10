# GATE-004I — aggregate identifier surplus

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `0<c<=1`, `B,delta>0`, and `n0` such that for
every `n>=n0`, every minimum circuit `C_n` for `SAT-gamma_n`, and

`ell(n)=max(1,floor(c log_2 n))`,

let `J_n={j:2^(ell(n)-1)<=j<2^ell(n)}`. If `q_j` is the size of the joint
semantic quotient under the ENC-008 pair `R_{j,0},R_{j,1}`, then

`sum_{j in J_n} (|C_n|-q_j) >= |J_n|(B n^delta+1)`.

Equivalently, after arbitrary LEMMA-013 representative assignments, the sum
of all disappeared-label incidences minus all split-label incidences meets
the same lower bound.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted SAT-gamma circuits; all equal-bit-length identifier-conditioned pairs; exact joint semantic quotients |
| Uniform/non-uniform | Fully non-uniform circuit adversary; aggregate covers every identifier in the chosen block |
| Circuit size | Average joint quotient loss at least `B n^delta+1` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed `c,B,delta>0`; every sufficiently large `n`; every minimum circuit; sum over all identifiers in the selected bit-length block |
| Regime | Worst-case exact total-language computation; malformed suffixes reject |

## Bridge

LEMMA-015 implies that one identifier has

`q_j<=|C_n|-B n^delta-1`,

which is GATE-004H. GATE-004H, ENC-008, and LEMMA-014 then establish the
nonterminal superlinear unrestricted SAT circuit lower bound GATE-004.

## Attack boundary

LEMMA-016 proves that the number of columns and their OR identities cannot
supply the aggregate inequality. The remaining obligation is a SAT-specific
row theorem: across the identifier block, parent labels that disappear must
outnumber split-label incidences by the displayed polynomial average. No such
row theorem is currently proved.
