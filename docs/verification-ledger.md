# Verification ledger

Passing repository checks certifies metadata consistency, not mathematical
truth. Each row has exactly one label.

| ID | Label | Result | Evidence | Terminal effect |
|---|---|---|---|---|
| INFRA-001 | PROVED | Required repository tree, policies, manifest, and cold-clone reproduction exist | `verification/audit.py`; `artifacts/cold-clone-a9865ce.md` | None |
| INFRA-002 | PROVED | Cycle-002 claim taxonomy and manifest reproduce from a cold clone | `artifacts/cold-clone-eb4ac30.md` | None |
| INFRA-003 | PROVED | Cycle-003 exact encoding, manifest, and reference tests reproduce from a cold clone | `artifacts/cold-clone-b8f06a0.md` | None |
| T-UNIFORM | EXPLORATORY | Open target: `SAT notin P` | `docs/problem-statement.md` | Not established |
| EQ-COOK | PROVED | `SAT notin P` is equivalent to `P != NP` under Cook-Levin | Cook problem statement/source note | Defines exact target |
| T-NONUNIFORM | EXPLORATORY | Open sufficient target: `SAT notin P/poly` | `docs/problem-statement.md` | Not established |
| BR-NONUNIFORM | PROVED | `SAT notin P/poly` implies `SAT notin P`, hence `P != NP` | Circuit unrolling plus EQ-COOK | Bridge only |
| ENC-001 | PROVED | `SAT-gamma` has a unique total parse, lies in NP, and is NP-hard | `docs/sat-encoding.md`; reference parser tests | Fixes the exact terminal representation |
| ENC-002 | PROVED | Double-NOT prefixes project every SAT slice into lengths larger by multiples of four | `docs/sat-encoding.md` | Supplies exact self-embeddings only |
| BARRIER-001 | PROVED | Major barrier/failure-mode audit | `docs/barrier-audit.md` and primary-source notes | Design constraints only |
| BRIDGE-001 | PROVED | SAT/Circuit-SAT bridge audit | `docs/bridge-audit.md` | Finds no closed terminal bridge |
| GATE-001 | NO-GO | Existing Williams-style transfer cannot be promoted directly to SAT outside P/poly | Quantifier and parameter audit | Prevents a circular promotion |
| GATE-002 | PROVED | Unbounded exponent ratio suffices to uniformize a hard-language family into one NP language outside P/poly | Human proof in `proofs/GATE-002-exponent-ratio-uniformization.md` | Conditional route; hypothesis unfilled |
| GATE-003-EQ | PROVED | GATE-003's unbounded-ratio family exists iff `NP notsubseteq P/poly` | GATE-002 plus repeated-language converse | Detects circular decomposition |
| GATE-003 | NO-GO | Reject the unbounded-ratio family as an intermediate brick | Equivalence GATE-003-EQ | No terminal credit |
| LEMMA-001 | PROVED | Reindexing and polynomial padding cannot increase the exponent ratio | `proofs/LEMMA-001-ratio-invariance.md` | Closes a reparameterization route |
| GATE-004A | NO-GO | Generic all-circuits constant-substitution gate elimination cannot prove a superlinear unrestricted SAT lower bound | GHKK16 method limitation | SAT-specific induction remains open |
| GATE-004 | EXPLORATORY | Prove a same-language superlinear unrestricted circuit lower bound for `SAT-gamma` | `proofs/GATE-004-sat-superlinear.md` | Active target; non-terminal alone |
| LEMMA-002 | PROVED | An `n^beta` length-loss / `n^(beta+delta)` gate-loss recurrence yields `Omega(n^(1+delta))` | `proofs/LEMMA-002-block-recurrence.md` | Closes quantitative summation step |
| GATE-004B-FANOUT | NO-GO | Exact projection plus generic boundary-fanout counting does not force the required gate loss | `proofs/GATE-004B-block-restriction.md` | SAT-specific circuit structure still open |
| GATE-004B | EXPLORATORY | Prove the SAT-specific amortized block-restriction inequality for minimum circuits | `proofs/GATE-004B-block-restriction.md` | Active smallest brick |
| GATE-005 | EXPLORATORY | Same-language exponent amplification for SAT | `proofs/GATE-005-same-language-amplification.md` | Downstream open bridge; not assumed |
| FORMAL-001 | EXPLORATORY | Formalize stable encoding and padding lemmas | `formal/README.md` | 0% formally closed chain |

There are no `FORMALLY VERIFIED` or `NUMERICAL` results at this commit.
