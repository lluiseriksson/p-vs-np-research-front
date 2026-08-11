# Cycle 185 — restriction-loss interface audit

**Label: PROVED**

LEMMA-219 constructs `m` binary gates that are exactly deleted at one
restriction yet remain essential to the unrestricted parent interface. At
`m=2`, exact two-gate loss still gives no free physical host.

## Classification

- LEMMA-219: `PROVED`
- GATE-004DL-RESTRICTION-LOSS-AS-FREE-HOST: `NO-GO`
- GATE-004DM: `EXPLORATORY`

GATE-004DM now requires four-code parent-preserving consumer certificates for
every host. No SAT lower bound or terminal implication is claimed.

`verification/restriction_lost_parent_essential_audit.py` checks `m=1,...,6`
zero-cofactor identities and selector-isolated essentiality. The exact-loss
and interface arguments are human proofs. Fable was not invoked; independent
certification is not performed.

## Model card

| Field | Value |
|---|---|
| Computational model | Uniform finite AND/OR restriction family plus the size-three endpoint host question |
| Uniform/non-uniform | Every `m>=1`; each witness non-uniform; endpoint target fully non-uniform |
| Circuit size | Witness `4m-1`; exactly `m` named restriction-lost gates |
| Circuit depth | Arbitrary OR-tree depth; target unrestricted |
| Fan-in | AND/OR two; NOT one allowed; fanout unrestricted |
| Randomness | None |
| Advice | None |
| Oracle access | None |
| Field/algebraic model | Exact Boolean restrictions and physical consumer interfaces |
| Asymptotic quantifiers | Every `m>=1`, every assignment, and every endpoint host candidate |
| Regime | Exact diagnostic theorem plus loss-to-host no-go; not a SAT lower bound or terminal result |
