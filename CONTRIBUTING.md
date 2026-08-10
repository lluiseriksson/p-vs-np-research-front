# Contribution protocol

1. State one falsifiable gate and give it an ID.
2. Add a complete model card to `verification/claims.json`.
3. Attempt the proof without weakening the statement silently.
4. Audit quantifiers, uniformity, reductions, and all applicable barriers.
5. Assign exactly one permitted label.
6. Update the verification and, when applicable, no-go ledgers.
7. Run `python verification/audit.py`.
8. Commit the brick and designate the next gate.

No restricted or conditional statement may be described as terminal progress
without an explicit proved implication to `T-UNIFORM` or a complete uniform
polynomial-time SAT algorithm.
