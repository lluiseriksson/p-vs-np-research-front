# Result-label policy

Each result has exactly one current label.

| Label | Meaning |
|---|---|
| `EXPLORATORY` | A question, conjecture, candidate mechanism, or incomplete argument |
| `NUMERICAL` | A finite computation or empirical observation; never an asymptotic proof |
| `CONDITIONAL` | A claimed application whose conclusion depends on a named unproved external hypothesis |
| `PROVED` | A complete human-audited mathematical theorem, including a universally quantified implication proved with its premises explicit, not yet kernel checked here |
| `FORMALLY VERIFIED` | A proof-assistant kernel has checked the exact statement and its axiom report is accepted |
| `NO-GO` | A precisely scoped route is blocked by a counterexample, barrier, quantifier loss, circularity, or inadequate parameters |

Promotion requires an explicit ledger edit and fresh audit evidence. Passing
`verification/audit.py` verifies repository structure and metadata only; it does
not promote mathematics.
