# Cycle 101 first-birth audit

## Localization

**Label: PROVED**

LEMMA-114 compares `alpha_empty` with `alpha_{ {i} }` at every circuit node.
The XOR difference is independent of `u_i` at all primary inputs and equals
`u_i` at the output. A first node where this dependence appears therefore
exists and is necessarily binary, because NOT preserves the XOR difference.

## Gate

**Label: EXPLORATORY**

GATE-004AJ asks to match the `m` indexed binary birth events injectively to
the `N` NOT gates or `t` cycle coordinates. This would prove the exact
standalone tradeoff through `m<=N+t`.

## Outcome

**Label: NO-GO**

The birth node itself cannot be the desired NOT witness. The trace must be
nonlocal and its reuse across indices must be bounded. No standalone circuit
lower bound, SAT lower bound, or terminal progress is claimed.
