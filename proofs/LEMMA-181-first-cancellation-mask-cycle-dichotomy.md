# LEMMA-181 — first cancellation is a mask or a surviving cycle

**Label: PROVED**

Assume the switching branch of LEMMA-180. Fix a directed path from the
earliest mixed NOT `n` to the output, let `d` be the first gate on that path
whose `01` and `11` cofactors are equal, let `p` be its preceding input on
the path, and let `q` be its other input. Then `d` is binary and exactly one
of these cases holds.

1. **One-sided mask:** `q_01=q_11=q`. If `d` is OR, then
   `p_01 XOR p_11 <= q`; if `d` is AND, then
   `p_01 XOR p_11 <= NOT q`.
2. **Two-sided cancellation:** `q_01!=q_11`. The two `u`-sensitive input
   branches into `d` create a nonzero undirected cycle coordinate in the
   parent output cone. Under the two-gate plateau, that coordinate survives
   every satisfying pair restriction modulo contractions.

## Proof

LEMMA-180 already proves that `d` is AND or OR and that
`p_01!=p_11`. The equality or inequality of the other two cofactors gives the
exhaustive cases.

In the mask case, OR equality says

`p_01 OR q = p_11 OR q`.

The two functions can differ only where `q=1`, which is the first displayed
containment. AND equality analogously says they can differ only where `q=0`.

In the two-sided case, both `p` and `q` depend essentially on `u` at `t=1`,
so each has a directed path from raw `u`. The union of those paths and their
two final edges into `d` contains two distinct undirected routes from their
last common vertex to `d`; hence it contains a nonzero cycle. LEMMA-178 says
that every satisfying restriction preserves the parent cycle rank. LEMMA-174
then says that no parent cycle coordinate is killed: the displayed coordinate
survives modulo contractions in each restricted minimum circuit.

## Model card

| Field | Value |
|---|---|
| Computational model | Minimum unrestricted plateau circuits at the first binary cancellation of two satisfying cofactors |
| Uniform/non-uniform | Every individual finite non-uniform switching-branch parent |
| Circuit size | No new gate bound; exact mask containment or persistent cycle coordinate |
| Circuit depth | Unrestricted |
| Fan-in | AND/OR two; NOT one; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Boolean symmetric difference and undirected cycle space over `F_2` |
| Asymptotic quantifiers | Every operational GATE-004CA switching path and every satisfying pair restriction |
| Regime | Exact local cancellation classification; not a branch exclusion, SAT lower bound, or terminal result |
