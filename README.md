# P versus NP Research Front

> **Status: EXPLORATORY. No proof of `P != NP` or `P = NP` is claimed.**

This is an independent, long-running research repository whose only terminal
objective is an unconditional, complete, non-circular, auditable resolution of
the standard P-versus-NP problem. Restricted-model lower bounds, oracle
separations, communication lower bounds, proof-complexity lower bounds,
algebraic-complexity lower bounds, experiments, and conditional consequences
remain non-terminal unless a fully proved bridge to the standard statement is
recorded.

## Fixed terminal target

The active branch is `P != NP`. Its exact terminal formulation is:

> There is no deterministic multitape Turing machine `M` and constant `c` such
> that `M` decides the fixed binary encoding of `SAT` on every input of length
> `n` in at most `n^c + c` steps.

Here `SAT` is the exact prefix language `SAT-gamma` specified in
[`docs/sat-encoding.md`](docs/sat-encoding.md); malformed strings reject.

By Cook-Levin NP-completeness, this is equivalent to `P != NP`. The stronger
terminal-sufficient theorem currently used in the vertical map is
`SAT notin P/poly`; the map records the explicit implication to the standard
uniform statement.

## Research discipline

The immutable work cycle is:

`brick -> audit -> commit -> ledger update -> next gate`

Every result receives exactly one label:

- `EXPLORATORY`
- `NUMERICAL`
- `CONDITIONAL`
- `PROVED`
- `FORMALLY VERIFIED`
- `NO-GO`

Labels are never promoted automatically. A proof is not `FORMALLY VERIFIED`
merely because repository checks pass; that label requires a proof-assistant
kernel check of the mathematical statement and an axiom audit.

Every canonical complexity claim has a machine-readable model card in
[`verification/claims.json`](verification/claims.json). The audit rejects a
claim missing its computational model, uniformity, size, depth, fan-in,
randomness, advice, oracle access, algebraic model, quantifiers, or case regime.

## Current vertical route

`P != NP <- SAT notin P <- SAT notin P/poly <- all same-language SAT circuit-exponent rungs`

The second audit proved that the proposed unbounded-ratio family GATE-003 is
equivalent to `NP notsubseteq P/poly`, so it is rejected as a circular
decomposition. Current SAT-algorithm transfers still do not close the terminal
arrow, and reindexing or padding their fixed-exponent NP lower bounds cannot
repair the exponent ratio. The active GATE-004 asks for a first same-language
superlinear unrestricted circuit lower bound for SAT; it is explicitly
non-terminal. See
[`docs/vertical-map.md`](docs/vertical-map.md) and
[`docs/no-go-ledger.md`](docs/no-go-ledger.md).

The third cycle fixed the exact `SAT-gamma` representation and reduced
GATE-004 to GATE-004B: a SAT-specific block projection must lose
`n^(beta+delta)` gates while shortening the encoding by only `O(n^beta)` bits.
The fourth cycle proved a broader exact prefix-context family, rejected the
tempting right-context analogue because it repairs some malformed strings, and
proved a general contiguous-placement coverage limit. Coordinate averaging
cannot force gate loss, so GATE-004C isolates the surviving semantic-loss
obligation for minimum SAT circuits.

The fifth cycle audits that semantic obligation against unrestricted sharing.
LEMMA-004 proves that minimality, essential prefix inputs, and even all `2^p`
distinct residual functions can coexist with only an `O(p)` size gap because a
large core survives every restriction. GATE-004D now states the precise
SAT-specific internal residual-collision surplus that would have to overcome
this obstruction.

The sixth cycle makes the parser-state attempt exact. ENC-004 supplies `k+1`
separated neutral prefixes of common length `12k`, all leaving the same SAT
suffix function. LEMMA-007 then proves that this entire output-level pattern,
even with every prefix bit essential, can retain an arbitrary shared core
behind an `O(k^2)` shell. GATE-004E isolates the still-open requirement inside
the cross-restriction table of internal SAT gate functions.

The seventh cycle exploits the neutral family’s exact block form `X*W*` and
reduces that shell to `3p+5` gates. This closes the generic cross-table route:
even all audited parser geometry can coexist with only linear prefix overhead.
GATE-004F now asks directly for a SAT-specific surplus of same-column internal
residual-function collisions.

The eighth cycle adds the adjacent annihilating context: changing two operator
bits turns the neutral SAT residual into constant zero. LEMMA-009 nevertheless
shows that a one-gate selector can place an arbitrary hard core next to a zero
cofactor without losing that core in the hard column. The full four-cofactor
operator-bit table is the next object under audit; GATE-004F remains open.

The ninth cycle computes that table exactly: one operator setting leaves SAT
and the other three give zero for every nonempty suffix. LEMMA-010 shows that a
three-gate one-hot selector realizes the complete pattern around any hard core.
Constant-width parser windows are therefore closed as a generic collision
source; the next GATE-004F attack moves to nonlocal prefix residuals.

The tenth cycle opens that nonlocal route. ENC-007 gives equal-length prefixes
for SAT conditioned on variable identifier 1 being false or true, whose OR is
exactly SAT. GATE-004G asks for a shared two-output quotient smaller than the
single parent circuit by `Omega(n^delta)`; this would directly yield GATE-004.
LEMMA-011 shows that branch distinctness, disjointness, and union alone do not
provide the gap, so the remaining obligation is explicitly SAT-internal.

The eleventh cycle closes a quantitative loophole in that route. LEMMA-012
shows that two restricted copies begin at `2S`; within-branch losses plus
cross-copy sharing must exceed the entire `S` duplication term before any
lower-bound surplus exists. Separately simplifying and ORing the branches is
therefore recorded as a no-go rather than a recurrence.

The twelfth cycle compares this obligation with primary multi-output
literature. Identical-copy amortized complexity is trivialized by arbitrary
fanout in general circuits, while NP-hardness of multi-output minimization is
not an explicit-function size lower bound. Neither result is promoted to the
conditioned-SAT gap.

The thirteenth cycle converts the joint gap into a signed parent-label count.
Each original gate represents zero, one, or two surviving residual classes;
the exact improvement is `disappeared labels - split labels`. Condition
sensitivity can create the negative split term and therefore cannot itself be
credited as progress. The next attack seeks a SAT-specific injection from split
labels into a larger disappeared set.

## Honest progress estimates

| Measure | Estimate | Meaning |
|---|---:|---|
| Infrastructure maturity | 50% | Repository, corrected target/bridge labels, exact bit-level SAT language, iterative parser/context/conditioned-residual tests, exact quotient and per-parent surplus accounting, expanded source audit, ledgers, model-card checker, manifest, and cold-clone audit exist; formal library and independent review remain immature. |
| Formally closed proof chain | 0% | No terminal-critical implication has been proof-assistant verified. |
| Real progress toward P vs NP | 0.00% | Quantifier, padding, generic gate-elimination, fanout, shared-core, parser lifting, conditioned-union, duplicated-branch, literature-promotion, and sensitivity-count failures are explicit; no new SAT lower bound or algorithm exists. |

These values are judgment calls, not metrics derived from files, tests, commits,
or special cases.

## Repository map

| Path | Purpose |
|---|---|
| `docs/problem-statement.md` | Exact standard target and encodings |
| `docs/sat-encoding.md` | Bit-level total SAT language used by every fine-grained claim |
| `docs/vertical-map.md` | Terminal-to-brick dependency map |
| `docs/barrier-audit.md` | Relativization, natural proofs, algebrization, diagonalization, circuit, uniformity, and reduction constraints |
| `docs/bridge-audit.md` | SAT/Circuit-SAT algorithm-to-lower-bound bridges and their terminal gaps |
| `docs/verification-ledger.md` | Result status and audit evidence |
| `docs/no-go-ledger.md` | Structural and quantitative failed routes |
| `docs/source-citations/` | Primary-source claim notes |
| `proofs/` | Human-readable gate statements and proof attempts |
| `formal/` | Proof-assistant boundary and future kernel-checked work |
| `verification/` | Machine-readable claims and deterministic audits |
| `experiments/` | Non-proof computational work, always separately labeled |
| `artifacts/` | Reproducibility manifests and auditable outputs |

Run the read-only audit with:

```powershell
python verification/audit.py
python -m unittest discover -s verification -p 'test_*.py' -v
```

## Adversarial stop condition

If a possible full solution appears, all expansion stops. The repository moves
to the protocol in [`docs/adversarial-protocol.md`](docs/adversarial-protocol.md):
circularity, relativization, natural-proofs, algebrization, quantifiers,
uniformity, reductions, primary literature, cold-clone reproduction, and formal
critical-step checks are audited before any manuscript or success claim.
