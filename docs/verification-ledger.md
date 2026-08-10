# Verification ledger

Passing repository checks certifies metadata consistency, not mathematical
truth. Each row has exactly one label.

| ID | Label | Result | Evidence | Terminal effect |
|---|---|---|---|---|
| INFRA-001 | PROVED | Required repository tree, policies, manifest, and cold-clone reproduction exist | `verification/audit.py`; `artifacts/cold-clone-a9865ce.md` | None |
| INFRA-002 | PROVED | Cycle-002 claim taxonomy and manifest reproduce from a cold clone | `artifacts/cold-clone-eb4ac30.md` | None |
| INFRA-003 | PROVED | Cycle-003 exact encoding, manifest, and reference tests reproduce from a cold clone | `artifacts/cold-clone-b8f06a0.md` | None |
| INFRA-004 | PROVED | Cycle-004 exact context audit, manifest, and eleven reference tests reproduce from a cold clone | `artifacts/cold-clone-14eb710.md` | None |
| INFRA-005 | PROVED | Cycle-005 semantic shared-core audit, manifest, and reference tests reproduce from a cold clone | `artifacts/cold-clone-5ed3e27.md` | None |
| INFRA-006 | PROVED | Cycle-006 neutral parser-state audit, manifest, and thirteen reference tests reproduce from a cold clone | `artifacts/cold-clone-17cab2f.md` | None |
| INFRA-007 | PROVED | Cycle-007 linear neutral-family audit, manifest, and fourteen reference tests reproduce from a cold clone | `artifacts/cold-clone-2d2b0de.md` | None |
| INFRA-008 | PROVED | Cycle-008 adjacent-annihilator audit, manifest, and fifteen reference tests reproduce from a cold clone | `artifacts/cold-clone-8797bc3.md` | None |
| INFRA-009 | PROVED | Cycle-009 full local cofactor audit, manifest, and sixteen reference tests reproduce from a cold clone | `artifacts/cold-clone-f444670.md` | None |
| INFRA-010 | PROVED | Cycle-010 conditioned-pair quotient audit, manifest, and seventeen reference tests reproduce from a cold clone | `artifacts/cold-clone-c101777.md` | None |
| INFRA-011 | PROVED | Cycle-011 joint-quotient accounting audit, manifest, and tests reproduce from a cold clone | `artifacts/cold-clone-6537f06.md` | None |
| INFRA-012 | PROVED | Cycle-012 multi-output literature audit, manifest, and tests reproduce from a cold clone | `artifacts/cold-clone-c2d3bb7.md` | None |
| INFRA-013 | PROVED | Cycle-013 signed parent-label audit, manifest, and tests reproduce from a cold clone | `artifacts/cold-clone-a839d1b.md` | None |
| INFRA-014 | PROVED | Cycle-014 many-identifier quotient audit, manifest, and tests reproduce from a cold clone | `artifacts/cold-clone-6bc7ef9.md` | None |
| INFRA-015 | PROVED | Cycle-015 cross-identifier incidence audit, manifest, and tests reproduce from a cold clone | `artifacts/cold-clone-f860c57.md` | None |
| T-UNIFORM | EXPLORATORY | Open target: `SAT notin P` | `docs/problem-statement.md` | Not established |
| EQ-COOK | PROVED | `SAT notin P` is equivalent to `P != NP` under Cook-Levin | Cook problem statement/source note | Defines exact target |
| T-NONUNIFORM | EXPLORATORY | Open sufficient target: `SAT notin P/poly` | `docs/problem-statement.md` | Not established |
| BR-NONUNIFORM | PROVED | `SAT notin P/poly` implies `SAT notin P`, hence `P != NP` | Circuit unrolling plus EQ-COOK | Bridge only |
| ENC-001 | PROVED | `SAT-gamma` has a unique total parse, lies in NP, and is NP-hard | `docs/sat-encoding.md`; reference parser tests | Fixes the exact terminal representation |
| ENC-002 | PROVED | Double-NOT prefixes project every SAT slice into lengths larger by multiples of four | `docs/sat-encoding.md` | Supplies exact self-embeddings only |
| ENC-003 | PROVED | Prefix tautology contexts and double negations give exact SAT-gamma slice projections | `docs/sat-encoding.md` | Broadens attainable prefix lengths only |
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
| LEMMA-003 | PROVED | Every sublinearly padded contiguous placement retains a common core, defeating arbitrary coordinate-weight coverage | `proofs/LEMMA-003-contiguous-context-coverage.md` | Method limitation only |
| GATE-004B-FANOUT | NO-GO | Exact projection plus generic boundary-fanout counting does not force the required gate loss | `proofs/GATE-004B-block-restriction.md` | SAT-specific circuit structure still open |
| GATE-004B | EXPLORATORY | Prove the SAT-specific amortized block-restriction inequality for minimum circuits | `proofs/GATE-004B-block-restriction.md` | Active parent gate |
| GATE-004B-RIGHT-CONTEXT | NO-GO | A fixed suffix context can repair malformed source syntax and is not an exact total-language projection | `docs/sat-encoding.md`; NG-009 | Prefix context remains exact |
| GATE-004B-CONTEXT-AVERAGING | NO-GO | Even hypothetical contiguous placements plus arbitrary coordinate-weight averaging cannot force positive loss | `proofs/LEMMA-003-contiguous-context-coverage.md` | Semantic or non-contiguous argument required |
| GATE-004C | EXPLORATORY | Prove semantic gate loss for minimum SAT circuits under the explicit ENC-003 context family | `proofs/GATE-004C-context-semantic-loss.md` | Active parent gate; sufficient for GATE-004B |
| LEMMA-004 | PROVED | Essential restricted inputs and all `2^p` distinct residuals can coexist with only an `O(p)` minimum-size gap | `proofs/LEMMA-004-shared-core-obstruction.md` | Generic shared-core limitation only |
| LEMMA-005 | PROVED | Exact residual-function quotienting preserves the restricted circuit output | `proofs/LEMMA-005-semantic-restriction-quotient.md` | Makes the semantic loss obligation exact |
| GATE-004C-GENERIC-SEMANTICS | NO-GO | Minimality, essentiality, and maximal input-residual diversity cannot generically force superlinear block loss | LEMMA-004; NG-011 | SAT-specific internal collisions required |
| GATE-004D | EXPLORATORY | Prove a superlinear surplus of constant, colliding, or dead internal residual gates under an exact SAT prefix restriction | `proofs/GATE-004D-sat-residual-collisions.md` | Active parent gate; sufficient for GATE-004C |
| ENC-004 | PROVED | For padding `12k`, `k+1` separated equal-length prefixes all preserve the exact SAT-gamma suffix function | `docs/sat-encoding.md`; LEMMA-006 | Supplies a concrete restriction family only |
| LEMMA-006 | PROVED | Neutral-prefix parser stacks and pairwise distances are exact | `proofs/LEMMA-006-neutral-prefix-family.md` | Output-level structure only |
| LEMMA-007 | PROVED | Separated neutral subcubes with essential prefix bits can retain an arbitrary shared core behind an `O(pr)` shell | `proofs/LEMMA-007-neutral-subcube-shared-core.md` | Generic shared-core limitation |
| GATE-004D-PARSER-LIFT | NO-GO | Neutral parser-state multiplicity and essentiality do not generically force internal collisions | LEMMA-007; NG-012 | SAT-specific internal property required |
| GATE-004E | EXPLORATORY | Prove the collision surplus within one explicit ENC-004 neutral-prefix family | `proofs/GATE-004E-neutral-family-collisions.md` | Active parent gate; sufficient for GATE-004D |
| LEMMA-008 | PROVED | The exact neutral family has a linear recognizer and can retain an arbitrary shared core behind a `3p+5`-gate shell | `proofs/LEMMA-008-regular-neutral-shared-core.md` | Sharpens the generic limitation |
| GATE-004E-CROSS-TABLE | NO-GO | Full output-level geometry and parser-state statistics of the neutral family do not generically force internal collisions | LEMMA-008; NG-013 | SAT-specific same-column property required |
| GATE-004F | EXPLORATORY | Prove many same-column internal residual gates become constant, input-equivalent, or mutually equivalent | `proofs/GATE-004F-same-column-collisions.md` | Open alternative route; sufficient for GATE-004E |
| ENC-005 | PROVED | A prefix two bits from the neutral context has constant-zero SAT-gamma residual | `docs/sat-encoding.md`; reference test | Supplies a local cofactor comparison only |
| LEMMA-009 | PROVED | Adjacent hard and zero cofactors can differ in minimum complexity by only one selector gate | `proofs/LEMMA-009-annihilating-cofactor-selector.md` | Generic selector limitation |
| GATE-004F-ANNIHILATOR | NO-GO | A nearby zero residual does not generically force loss inside the retained hard column | LEMMA-009; NG-014 | Full SAT-specific cofactor structure remains open |
| ENC-006 | PROVED | The complete local operator-bit square has one SAT residual and three zero residuals | `docs/sat-encoding.md`; reference test | Exact local output table only |
| LEMMA-010 | PROVED | A one-hot two-bit selector retains an arbitrary hard core with only three gates overhead | `proofs/LEMMA-010-one-hot-cofactor-selector.md` | Generic selector limitation |
| GATE-004F-FOUR-COFACTOR | NO-GO | The complete local one-hard/three-zero cofactor table does not force hard-column loss | LEMMA-010; NG-015 | A nonlocal SAT-specific invariant is required |
| ENC-007 | PROVED | Equal-length prefixes produce SAT conditioned on variable 1 false/true, whose OR is exact SAT | `docs/sat-encoding.md`; reference test | Supplies a nonlocal two-output decomposition |
| LEMMA-011 | PROVED | Distinct disjoint conditioned branches can share an arbitrary hard core with constant overhead | `proofs/LEMMA-011-conditioned-union-shared-core.md` | Generic direct-sum limitation |
| GATE-004G-CONDITIONED-UNION | NO-GO | Conditioned-branch distinctness, disjointness, and union identity do not force joint compression | LEMMA-011; NG-016 | SAT-specific internal sharing must be controlled |
| GATE-004G | EXPLORATORY | Jointly quotient both conditioned SAT residuals below the parent circuit by `B n^delta+1` gates | `proofs/GATE-004G-joint-conditioned-quotient.md` | Active smallest brick; directly sufficient for GATE-004 |
| LEMMA-012 | PROVED | Exact joint-quotient accounting requires within-branch loss plus cross-sharing to exceed the full duplicated parent size | `proofs/LEMMA-012-joint-quotient-accounting.md` | Quantifies the missing surplus |
| GATE-004G-SEPARATE-LOSSES | NO-GO | Separately simplifying and ORing two copies fails unless the entire parent-size duplication term is paid | LEMMA-012; NG-017 | Joint SAT-specific sharing remains open |
| BR-RZ21 | PROVED | Formal measures characterize identical-copy amortized complexity; arbitrary fanout trivializes it for general circuits | RZ21 primary-source note | Literature boundary only |
| BR-ILO20 | PROVED | Minimizing truth-table-given total multi-output functions is NP-hard under randomized reductions | ILO20 primary-source note | No explicit-function lower bound |
| GATE-004G-LITERATURE | NO-GO | Neither amortized-copy duality nor multi-output minimization hardness proves the conditioned-SAT joint gap | Bridge audit; NG-018 | Explicit SAT-specific surplus remains open |
| LEMMA-013 | PROVED | Joint improvement equals disappeared parent labels minus labels representing two split residual classes | `proofs/LEMMA-013-parent-label-surplus.md` | Exact signed-surplus normal form |
| GATE-004G-SENSITIVITY | NO-GO | Condition-sensitive gate counts alone do not force a favorable disappeared-minus-split balance | LEMMA-011; NG-019 | A SAT-specific structural injection is required |
| ENC-008 | PROVED | Every identifier bit-length block supplies exponentially many equal-length conditioned SAT pairs | `docs/sat-encoding.md`; reference test | Projection supply only |
| LEMMA-014 | PROVED | An `n^delta` gain per `O(log n)` length loss yields `Omega(n^(1+delta)/log n)` size | `proofs/LEMMA-014-logarithmic-step-recurrence.md` | Closes the logarithmic-step summation |
| GATE-004H | EXPLORATORY | Choose one identifier among polynomially many whose joint conditioned quotient has `B n^delta` net loss | `proofs/GATE-004H-many-identifier-conditioned-quotient.md` | Active smallest brick; sufficient for GATE-004 |
| LEMMA-015 | PROVED | Identifier-by-parent-label incidences sum exactly to the aggregate joint-quotient improvement | `proofs/LEMMA-015-identifier-incidence-averaging.md` | Exact averaging reduction |
| LEMMA-016 | PROVED | Arbitrarily many distinct paired prefixes can retain one shared core with zero quotient loss | `proofs/LEMMA-016-many-prefix-shared-core.md` | Generic multiplicity obstruction |
| GATE-004H-CANDIDATE-COUNT | NO-GO | Candidate count and OR reconstruction alone do not imply a favorable quotient column | LEMMA-016; NG-020 | SAT-specific signed surplus is required |
| GATE-004I | EXPLORATORY | Prove polynomial average signed quotient loss across an identifier block | `proofs/GATE-004I-aggregate-identifier-surplus.md` | Active smallest brick; sufficient for GATE-004H |
| LEMMA-017 | PROVED | Essential dependence on every prefix bit can be confined to an `O(p)` parity-selector shell | `proofs/LEMMA-017-essential-prefix-selector-shell.md` | Generic essentiality obstruction |
| GATE-004I-PREFIX-ESSENTIALITY | NO-GO | Prefix essentiality plus many reconstructing pairs does not imply polynomial aggregate surplus | LEMMA-017; NG-021 | Conditioned-SAT internal structure remains necessary |
| GATE-005 | EXPLORATORY | Same-language exponent amplification for SAT | `proofs/GATE-005-same-language-amplification.md` | Downstream open bridge; not assumed |
| FORMAL-001 | EXPLORATORY | Formalize stable encoding and padding lemmas | `formal/README.md` | 0% formally closed chain |

There are no `FORMALLY VERIFIED` or `NUMERICAL` results at this commit.
