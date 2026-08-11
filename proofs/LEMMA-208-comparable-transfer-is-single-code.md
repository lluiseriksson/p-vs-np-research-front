# LEMMA-208 — comparable specialization changes one exterior code only

**Label: PROVED**

Use the setup of LEMMA-207. The comparable boundary selects
`sigma in {0,1}` and replaces the region output `r` by the global cofactor
`r|_{u=sigma}`. For every physical gate outside the specialized region, its
function before and after specialization can differ only at the single code

`(u,t)=(1-sigma,0)`.

Equivalently:

- if `sigma=0`, every exterior `00`, `01`, and `11` cofactor is unchanged and
  only the unsatisfying `10` cofactor may change;
- if `sigma=1`, every exterior `10`, `01`, and `11` cofactor is unchanged and
  only the satisfying `00` cofactor may change.

Every gate on a LEMMA-207 changed path differs at that code and nowhere else.
In particular, a newly counted boundary input `q` is created by changing
exactly one member of its formerly equal pair `(q_00,q_10)`.

## Proof

At the interface signal, the specialized function has cofactors

`r^sigma_{u,t}=r_{sigma,t}`.

When `u=sigma`, this equals the original cofactor by definition. When `t=1`,
LEMMA-203 gives `r_01=r_11`, so it also equals the original cofactor for both
values of `u`. The only code not covered by these two equalities is
`(1-sigma,0)`. Thus the claim holds at `r`.

Order the exterior gates topologically. Raw inputs and every exterior signal
not reachable from `r` are unchanged. Suppose inductively that every input of
an exterior gate has the same before/after cofactors at all codes except
possibly `(1-sigma,0)`. Applying the same deterministic AND, OR, or NOT
operation to equal input values gives equal output values at each of the other
three codes. This proves the claim for the gate, even if two changed branches
reconverge. Induction proves the exterior statement.

A gate belongs to the changed set precisely when its before/after functions
are not equal. Since equality is already proved on three codes, every changed
gate differs on the remaining code. LEMMA-207 shows that a newly counted
input `q` changes from `q_00=q_10` to unequal row-zero cofactors. The unchanged
member is the one with `u=sigma`; hence exactly the other member changed.

## Model card

| Field | Value |
|---|---|
| Computational model | Two finite unrestricted AND/OR/NOT DAGs with the same physical exterior and one comparable cofactor specialization |
| Uniform/non-uniform | Every finite non-uniform LEMMA-207 specialization and every exterior gate |
| Circuit size | Specialized circuit has size at most the parent; no size lower bound follows |
| Circuit depth | Unrestricted; proof is topological induction over arbitrary finite depth |
| Fan-in | AND/OR two; NOT one; reconvergent changed branches allowed |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact four-code Boolean cofactors |
| Asymptotic quantifiers | Every qualifying boundary, both `sigma` values, every exterior gate, and every base assignment |
| Regime | Exact worst-case code-localization theorem; not a pruning-cost theorem, plateau exclusion, SAT lower bound, or terminal result |
