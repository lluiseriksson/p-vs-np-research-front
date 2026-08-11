# Cycle 194 — oriented support-threshold audit

**Label: PROVED**

LEMMA-231 combines exact carrier loss identities with a marked physical gate
support. More than four marked gates in AND→OR or six in OR→AND leaves a named
gate present in all three satisfying minors.

LEMMA-232 proves these thresholds sharp using loss sets alone. Thus
GATE-004DU-LONG-SUPPORT-PIGEONHOLE-ONLY is `NO-GO` (NG-170): bounded cores
remain, and abstract set systems do not settle Boolean realizability.
GATE-004DV asks for a semantics-preserving port reduction and classification
of cores of size at most four or six.

## Classification

- LEMMA-231: `PROVED`
- LEMMA-232: `PROVED`
- GATE-004DU-LONG-SUPPORT-PIGEONHOLE-ONLY: `NO-GO`
- GATE-004DV: `EXPLORATORY`

`verification/oriented_support_threshold_audit.py` exhausts two-element loss
sets on eight symbols and verifies both maximum unions and threshold
witnesses. The endpoint inequality is a human set proof from LEMMA-193/218.
Fable was not invoked; independent certification and terminal implications
are not claimed.

## Model card

| Field | Value |
|---|---|
| Computational model | Exact oriented physical loss sets and marked support gates |
| Uniform/non-uniform | Every hypothetical endpoint for the theorem; finite abstract set witnesses |
| Circuit size | Parent `K+2`; union caps four/six; bounded residual cores four/six |
| Circuit depth | Unrestricted target; not applicable to set witnesses |
| Fan-in | Target AND/OR two and NOT one; set audit fan-in independent |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Finite physical gate sets and cardinality |
| Asymptotic quantifiers | Every marked support, both orientations, and every enumerated two-element set |
| Regime | Exact threshold and set-sharpness audit; not Boolean endpoint realizability, SAT lower bound, or terminal result |
