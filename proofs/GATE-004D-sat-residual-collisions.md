# GATE-004D — SAT residual-function collision surplus

**Label: EXPLORATORY**

## Falsifiable theorem

There exist explicit constants `A,B>0`, `0<=beta<1`, `delta>0`, and `n0`
such that for every `n>=n0` and every minimum-size circuit `C_n` for
`SAT-gamma_n`, there is an exact ENC-003 prefix restriction to some
`m` satisfying `n-A n^beta<=m<n` whose semantic restriction quotient from
LEMMA-005, including constant normalization, has at most

`|C_n|-B n^(beta+delta)`

gates.

Equivalently, the restriction must create enough constant residual gates,
residual-function collisions, or dead gates to exceed the shared-core shell by
the displayed amount.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted Boolean circuits for exact SAT-gamma slices; ENC-003 prefix restrictions; semantic quotient |
| Uniform/non-uniform | Fully non-uniform circuit adversary and restriction choice; quotient is existential |
| Circuit size | Quotient loses at least `B n^(beta+delta)` gates after at most three constant-normalization gates |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one |
| Randomness | None |
| Advice | No verifier advice; restriction may depend non-uniformly on the circuit |
| Oracle access | None |
| Field/algebraic model | None |
| Asymptotic quantifiers | Exists fixed constants; every sufficiently large `n`; every minimum circuit; exists one exact prefix restriction |
| Regime | Worst-case exact total-language computation; malformed encodings reject |

## Bridge

LEMMA-005 turns the quotient into a circuit for `SAT-gamma_m`. Therefore
GATE-004D implies GATE-004C, which implies GATE-004B. LEMMA-002 then yields
GATE-004. No terminal amplification is supplied.

## First audit

LEMMA-004 rules out three generic substitutes for the required collision
surplus. A function can have a minimum-size gap of only `O(p)` across every
`p`-bit restriction even when all restricted coordinates are essential and all
`2^p` residual functions are distinct. The reason is unrestricted sharing: a
large `G(u)` core survives every restriction while only an `O(p)` shell changes.

Thus GATE-004D must establish a SAT-specific fact about residual functions of
*internal gates* in every minimum circuit. Counting input residuals, proving
input influence, or invoking circuit minimality alone is quantitatively
insufficient. The next attack is to test whether parser-state descendants force
such internal collisions; absent that bridge, the gate remains open.
