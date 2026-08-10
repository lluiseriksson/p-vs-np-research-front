# GATE-004AL-LEMMA111-ONLY — generic restriction proves quintet Hall

**Label: NO-GO**

Restricting to a five-index set and applying only the all-DAG
cycle-rank/inversion bound from LEMMA-111 does not prove the required Hall
union size five. Its exact resource surplus is

`g(5)=min_{c>=0} [c+max(ceil(5/2^c),ceil(log_2(6)))] = 4`,

attained at `c=1`, where the bound permits `q=3` NOT gates. Thus the method
certifies only

`|union_{i in I} P_i(T)| >= q+c >= 4`

for a quintet, one below Hall's requirement.

This is a quantitative method no-go, not a circuit counterexample. It does
not show that a deficient quintet exists. A proof of the size-five inequality
must use dependency-cone incidence beyond total residual cycle rank and
inversion complexity. GATE-004AL and all larger gates remain open.

LEMMA-117 records the equality case forced by any actual deficient quintet:
`c=1,q=3`. GATE-004AM now asks to exclude that exact stratum by
function-specific means.

## Model card

| Field | Value |
|---|---|
| Computational model | Five-block restrictions of unrestricted circuits followed by generic cycle-rank unfolding and inversion bounds |
| Uniform/non-uniform | Every individual non-uniform parent circuit; method audit for arbitrary five-index subsets |
| Circuit size | Generic resource lower bound four versus Hall target five |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Undirected cycle space over `F_2` and Boolean-lattice inversion |
| Asymptotic quantifiers | Every parent size `m>=5` and every selected set of exactly five clause indices |
| Regime | Quantitative no-go for LEMMA-111 alone; dependency-specific quintet expansion remains open |
