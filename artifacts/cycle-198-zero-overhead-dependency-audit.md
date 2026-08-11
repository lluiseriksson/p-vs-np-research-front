# Cycle 198 — zero-overhead coordinate dependencies

**Label: PROVED**

LEMMA-238 characterizes `h=0` exactly by a coordinate straight-line ordering.
LEMMA-239 shows why this is not yet a payment theorem: a minimum vector can
have zero overhead while all of its coordinate gates form one arbitrarily
long dependency chain. Counting those gates as independent hosts is NG-174.

LEMMA-240 supplies the surviving quantitative structure. For dependency
height `H`, width `W`, and `q` coordinate gates, `q<=HW`. GATE-004DZ asks the
endpoint-specific question that the poset theorem cannot answer: turn a wide
antichain or long chain into named physical payments, or reduce the remainder
to fewer than `D^2` fully labeled coordinate gates.

## Classification

- LEMMA-238: `PROVED`
- LEMMA-239: `PROVED`
- LEMMA-240: `PROVED`
- GATE-004DY-ZERO-OVERHEAD-AS-INDEPENDENT-HOSTS: `NO-GO`
- GATE-004DY: `EXPLORATORY`
- GATE-004DZ: `EXPLORATORY`

`verification/zero_overhead_dependency_audit.py` checks the nested family
through `m=8` and the height-width inequality over every naturally ordered DAG
through five vertices. The general results use the displayed structural
proofs. Fable was not invoked; independent certification, endpoint payment,
and terminal implications are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Constant-free multi-output AND/OR/NOT coordinate DAGs and refined zero-overhead endpoint regions |
| Uniform/non-uniform | Every finite vector for the structural theorems; every finite non-uniform residual endpoint for GATE-004DZ |
| Circuit size | Exact equality `C_A(P)=q`; nested cost `m`; dependency inequality `q<=HW` |
| Circuit depth | Unrestricted; nested witness depth `m` and general height `H` explicit |
| Fan-in | AND/OR two; NOT one; fanout and coordinate dependencies unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean vectors, reachability posets, and endpoint cycle spaces over `F_2` |
| Asymptotic quantifiers | Every finite vector/DAG, every `m>=1`, and every residual endpoint branch |
| Regime | Exact structural lemmas and scoped no-go; not endpoint proof, SAT lower bound, or terminal result |
