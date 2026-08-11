# Cycle 147 — earliest-NOT signature dichotomy

**Label: PROVED**

LEMMA-180 proves that the input of the earliest `u`-sensitive NOT is monotone
in `u`, so its output cofactors are ordered. The NOT either has one stable
signature across satisfying codes `01,11`, or its difference is erased at a
first binary cancellation gate before the equal output cofactors.

GATE-004BZ-COFACTOR-ORDER-ONLY is `NO-GO`: a constant-size Boolean gadget
masks a strict ordered difference at one OR gate. GATE-004CA is the next
exact gate and asks whether pair minimality plus the fourth zero cofactor
excludes this switching/cancellation branch.

## Classification

- LEMMA-180: `PROVED`
- GATE-004BZ-COFACTOR-ORDER-ONLY: `NO-GO`
- GATE-004CA: `EXPLORATORY`
- GATE-004BZ: remains `EXPLORATORY`
