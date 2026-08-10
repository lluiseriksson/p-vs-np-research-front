# Cycle 099 canonical cofactor audit

## Primary-literature scope audit

**Label: PROVED**

Fischer's negation normalization and He–Liang–Sarma's bounded-treewidth study
confirm that low negation count alone cannot be promoted to an unrestricted
size lower bound. Neither source supplies the exact linear binary/NOT
tradeoff required here.

## Cofactor theorem

**Label: PROVED**

LEMMA-112 determines all `2^m` canonical positive cofactors exactly. Cofactor
`S` is `AND_{i in S} NOT u_i` and has size `|S|`; the maximum is `m` and the
average is `m/2`.

## Gate and method outcome

**Label: NO-GO**

GATE-004AH isolates the missing function-specific inequality
`B+N>=6m-1` throughout the intermediate NOT range. Independent cofactor
charging cannot prove it: maximum and average residual sizes are too small,
and summing across mutually exclusive restrictions would double count parent
gates. GATE-004AH/AG/AE remain `EXPLORATORY`; no terminal progress is claimed.
