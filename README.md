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

`P != NP <- SAT notin P <- SAT notin P/poly <- a single NP language outside P/poly <- quantifier-stable lower-bound gate`

The first audit found that current SAT-algorithm transfers do not close the last
arrow. In particular, fixed-exponent NP circuit lower bounds cannot be silently
uniformized into `NP notsubseteq P/poly`. See
[`docs/vertical-map.md`](docs/vertical-map.md) and
[`docs/no-go-ledger.md`](docs/no-go-ledger.md).

## Honest progress estimates

| Measure | Estimate | Meaning |
|---|---:|---|
| Infrastructure maturity | 28% | Repository, ledgers, source audit, model-card checker, and first gate cycle exist; formal library and cold-clone CI remain immature. |
| Formally closed proof chain | 0% | No terminal-critical implication has been proof-assistant verified. |
| Real progress toward P vs NP | 0.00% | A known quantifier/padding failure has been made explicit; no new terminal lower bound or algorithm exists. |

These values are judgment calls, not metrics derived from files, tests, commits,
or special cases.

## Repository map

| Path | Purpose |
|---|---|
| `docs/problem-statement.md` | Exact standard target and encodings |
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
```

## Adversarial stop condition

If a possible full solution appears, all expansion stops. The repository moves
to the protocol in [`docs/adversarial-protocol.md`](docs/adversarial-protocol.md):
circularity, relativization, natural-proofs, algebrization, quantifiers,
uniformity, reductions, primary literature, cold-clone reproduction, and formal
critical-step checks are audited before any manuscript or success claim.
