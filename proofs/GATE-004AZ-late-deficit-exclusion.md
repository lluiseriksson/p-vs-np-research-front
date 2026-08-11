# GATE-004AZ — exclude late implication savings

**Label: EXPLORATORY**

Use the canonical implication sequence and deficits `Delta_j` of LEMMA-152.
Let

`r=max({j in {1,...,m}: Delta_j>Delta_{j-1}} union {0})`

be the last clause count at which the deficit increases.

## Falsifiable theorem

Prove

`r<=Delta_m+K`.

A compatible canonical family with a deficit increase after
`Delta_m+K` falsifies the theorem.

## Exact bridge to GATE-004AX

After index `r`, every deficit increment is zero. Start with any minimum
circuit for `J_r` and repeatedly apply LEMMA-152. The resulting circuit for
`J_m` is minimum, gains four quotient classes at every extension, and keeps
the same collision count.

LEMMA-145 and LEMMA-144 at implication width `p=1` give `Q_r>=3r`; trivially
`b_r<=r`. Therefore the final minimum circuit satisfies

`Q_m-b_m>=3r-r+4(m-r)=4m-2r`.

If the proposed late-savings bound holds, then

`Q_m-b_m>=4m-2(Delta_m+K)`,

which is exactly GATE-004AX and hence GATE-004AY.

The zero-deficit case has `r=0` and recovers GATE-004AY-ZERO-DEFICIT. The new
content is that every positive saving must occur within the first
`Delta_m+K=O(K)=o(m)` clause counts. A proof must use symmetry, replication,
or localization of circuit savings; the scalar recurrence alone is
insufficient.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted canonical circuits along the nested implication-clause sequence |
| Uniform/non-uniform | Uniform canonical base/rows and symmetric fresh clauses; fully non-uniform minimum circuit at each size |
| Circuit size | Deficits `Delta_j=K+3j-C(J_j)`; target last increase `r<=Delta_m+K` |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Integer deficit recurrence and Boolean quotient extensions only |
| Asymptotic quantifiers | Every sufficiently large compatible canonical instance and every prefix length `0<=j<=m` |
| Regime | Exact sufficient positive-deficit subgate for GATE-004AX; not a SAT lower bound or terminal result |
