# Cycle 171 — private comparable counterflow audit

**Label: PROVED**

LEMMA-205 proves an exact basis-level exchange for comparable counterflow when
an explicit cofactor-private region exists. Meet/join selects one global
cofactor of `r`; specializing raw `u` inside the private region cannot add
gates and strictly lowers size or `R_0`.

A shared-fanout gadget shows that comparability does not permit globally
replacing `r`: a second live consumer changes. This is a local nonminimal
witness and does not rule out all edge-local rewrites.

A finite regression checked all 64 assignments of the shared-fanout witness,
including the displayed assignment on which global specialization changes the
downstream output. The human substitution proof, not this finite regression,
carries the `PROVED` label.

## Classification

- LEMMA-205: `PROVED`
- GATE-004CX-GLOBAL-SPECIALIZATION-ONLY: `NO-GO`
- GATE-004CY: `EXPLORATORY`

The residual gate separates shared comparable cones from incomparable
row-zero cofactors. No plateau exclusion, SAT lower bound, or terminal
implication is claimed.
