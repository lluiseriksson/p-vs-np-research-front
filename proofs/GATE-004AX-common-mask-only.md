# GATE-004AX-COMMON-MASK-ONLY — normalize every collision to an exposed OR mask

**Label: NO-GO**

LEMMA-148 excludes two or more exposed clause-local collision gates sharing
one exact OR mask in a minimum circuit. It does not apply to an arbitrary gate
whose selected-row cofactor is raw `t_i`.

Indeed, let `S(X)` vanish on the two selected rows and be one elsewhere, and
put

`g=t_i XOR S`.

Then both selected cofactors of `g` are `t_i`, but `g` cannot equal
`t_i OR R(X)` for any base-only `R`: when `S=1,t_i=1`, `g=0`, whereas every
such OR is one. Nor can it equal `t_i AND R(X)`: when `S=1,t_i=0`, `g=1`,
whereas every such AND is zero. XOR has a constant-size AND/OR/NOT
implementation. Cofactor equality therefore supplies no common-mask normal
form. It also supplies no exposed-use condition; the witness gate may fan out
or enter mixed subgraphs.

Assuming exact OR masks, commonality, and clause-local exposed uses for all
collisions would insert the missing structural conclusion. The common-mask
exchange is valid once those premises are proved, but cannot prove
GATE-004AX by itself. The next attack must derive a minimum-circuit collision
normal form or charge every failure of that form directly to quotient surplus
or to the `Delta+K` slack.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted implication circuits audited by a restricted exposed common-mask rewrite |
| Uniform/non-uniform | Fully non-uniform circuit adversary and finite semantic counterexample to the normalization inference |
| Circuit size | LEMMA-148 saves `b-1` only inside the exposed form; arbitrary XOR-type witnesses have constant overhead |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean cofactors and distributivity; XOR only as an AND/OR/NOT-definable witness function |
| Asymptotic quantifiers | Every selected row pair admitting a nonzero vanishing predicate; arbitrary collision witnesses outside the exposed form |
| Regime | Structural no-go for common-mask-only normalization; GATE-004AX/AW/AV/AU/AG/AE remain open |
