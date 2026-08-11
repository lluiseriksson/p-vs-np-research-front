# GATE-004BG-NOT-SPLIT-ONLY — infer survival from the exact regional counts

**Label: NO-GO**

LEMMA-160's equalities specify only how many NOT occurrences lie upstream and
downstream. They do not specify the parent functions of those occurrences or
their behavior under a neutral restriction.

For example, each occurrence that specializes to `NOT u_i` after a base
cofactor may globally compute `NOT(u_i OR R_i(X_base))`, as in
GATE-004BF-RESIDUAL-LOCALITY-ONLY. Replacing `a` or `b` abstractly allocated
labels by such mixed functions preserves the same regional count. The count
does not say whether a second output path retains the occurrence or the cycle
after its clause is neutralized.

No minimum unicyclic realization of all these mixed labels is asserted. This
closes only the inference from the exact pair of integers `(a,b)` or
`(p,j-p)` to resource survival. GATE-004BG requires the actual two-path wiring
from LEMMA-120.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract regional NOT allocations decorated by Boolean mixed gate functions |
| Uniform/non-uniform | Explicit non-uniform semantic abstraction; no minimum-circuit realization claim |
| Circuit size | Exact LEMMA-160 regional counts; no parent total-size assertion beyond the abstraction |
| Circuit depth | Unrestricted ambient formulas |
| Fan-in | OR two; NOT one; target circuit otherwise binary AND/OR |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and integer regional counts only |
| Asymptotic quantifiers | Every permitted no-cut or sole-cut count split |
| Regime | Structural no-go for NOT-split-only survival; GATE-004BG/BF are later proved using tree wiring and LEMMA-163, while GATE-004BE/BD/BA/AZ/AY/AX/AW/AV/AU/AG/AE remain open |
