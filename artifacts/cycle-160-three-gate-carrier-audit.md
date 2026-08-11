# Cycle 160 — three-gate carrier audit

**Label: PROVED**

LEMMA-193 classifies every size-three switching carrier as an alternating
binary chain before the earliest mixed NOT. AND→OR forces
`E_00=E_01={g,h}`; OR→AND forces `E_11={g,h}`. These codes exhaust their exact
two-gate deletion budgets on the carrier pair.

The local AND→OR gadget and its dual realize the cofactor and contraction
pattern without realizing a minimum plateau. Therefore local alternation is
`NO-GO` as a contradiction. GATE-004CN is active and must use all fanout exits
and cross-code output equality.

## Classification

- LEMMA-193: `PROVED`
- GATE-004CM-SIZE-THREE-LOCAL-ONLY: `NO-GO`
- GATE-004CN: `EXPLORATORY`
