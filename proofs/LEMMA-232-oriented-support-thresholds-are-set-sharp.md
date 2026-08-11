# LEMMA-232 — the oriented support thresholds are sharp as set systems

**Label: PROVED**

The bounds four and six in LEMMA-231 cannot be improved using only the exact
loss-set cardinalities and carrier equalities.

For AND→OR, take distinct physical symbols `g,h,a,b` and

```text
L_00=L_01={g,h},  L_11={a,b},  X={g,h,a,b}.
```

For OR→AND, take distinct symbols `g,h,a,b,c,d` and

```text
L_11={g,h},  L_00={a,b},  L_01={c,d},
X={g,h,a,b,c,d}.
```

Each system obeys the exact two-element loss identities and its union covers
`X`. Thus no common surviving gate follows at support size four or six from
set data alone.

These are abstract physical-identity set systems, not circuits. They do not
prove that the full-coverage patterns satisfy the four-code swap signatures,
cycle contractions, or endpoint minimality.

## Model card

| Field | Value |
|---|---|
| Computational model | Abstract exact physical loss-set systems for both size-three carrier orientations |
| Uniform/non-uniform | Two finite non-uniform set witnesses |
| Circuit size | Four symbols in AND→OR and six in OR→AND; every loss set has size two |
| Circuit depth | Not applicable to set witnesses; target depth unrestricted |
| Fan-in | Set theorem; target circuit retains AND/OR two and NOT one |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite physical gate sets; no algebraic computation |
| Asymptotic quantifiers | Both orientations and every symbol in the displayed systems |
| Regime | Exact set-sharpness witness; not Boolean endpoint realizability, SAT lower bound, or terminal result |
