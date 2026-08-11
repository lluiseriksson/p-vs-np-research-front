# Cycle 196 — global port-quotient audit

**Label: PROVED**

LEMMA-234 records the unrestricted corollary of LEMMA-005: reachable gates in
a minimum circuit have pairwise distinct global Boolean functions.

LEMMA-235 shows why this quotient does not finish the port reduction. The
fixed-core diagnostic has `m` pairwise distinct port functions for arbitrary
`m`. Thus GATE-004DW-GLOBAL-FUNCTION-QUOTIENT-ONLY is `NO-GO` (NG-172).
GATE-004DX replaces class counting by exact minimum joint cost of the complete
port-transfer vector.

## Classification

- LEMMA-234: `PROVED`
- LEMMA-235: `PROVED`
- GATE-004DW-GLOBAL-FUNCTION-QUOTIENT-ONLY: `NO-GO`
- GATE-004DX: `EXPLORATORY`

`verification/global_port_quotient_audit.py` checks pairwise distinction and
nonconstancy through `m=10`. The general statements have direct assignment
and topological-redirection proofs. Fable was not invoked; independent
certification and terminal implications are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted AND/OR/NOT semantic quotient plus the uniform fixed-core port family |
| Uniform/non-uniform | Every finite minimum circuit; every finite diagnostic `m>=1` |
| Circuit size | Duplicate removal saves one gate; diagnostic leaves at least `m` port classes |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact global Boolean functions and semantic quotient classes |
| Asymptotic quantifiers | Every duplicate gate pair and every diagnostic port pair |
| Regime | Exact quotient theorem and quantitative no-go; not a SAT lower bound or terminal result |
