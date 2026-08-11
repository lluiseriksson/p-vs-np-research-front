# Cycle 145 — three-code plateau rigidity

**Label: PROVED**

LEMMA-178 audits the exact failure case of GATE-004BX. A two-gate implication
increment would make all three satisfying restrictions minimum base circuits,
with identical NOT count and cycle rank, while deleting exactly two binary
gates. Yet every parent has at least three pair-sensitive gates, so some pair
dependence must survive as base computation in each code.

GATE-004BX-EXPOSED-TWO-GATE-SHELL-ONLY is `NO-GO`: the hypothetical saving,
if real, is necessarily interleaved. GATE-004BY selects a parent minimizing
pair-sensitive gates and asks for a same-size uncrossing rewrite that lowers
that finite potential.

## Classification

- LEMMA-178: `PROVED`
- GATE-004BX-EXPOSED-TWO-GATE-SHELL-ONLY: `NO-GO`
- GATE-004BY: `EXPLORATORY`
- GATE-004BX: remains `EXPLORATORY`
