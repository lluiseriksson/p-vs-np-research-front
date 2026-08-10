# SW09 — fixed-polynomial size circuit bounds

Rahul Santhanam and Ryan Williams, “On the Possibility of Fixed-Polynomial Size
Circuit Lower Bounds,” conference paper/preprint.

- Author PDF: https://people.csail.mit.edu/rrw/circuit.pdf
- Accessed: 2026-08-10
- Consumed claims: fixed-exponent lower bounds have translation theorems that
  differ sharply from superpolynomial lower bounds; Theorem 11 translates
  `NP notsubseteq SIZE(n^k)` to an oblivious-NP/one-bit-advice formulation at
  the same fixed exponent.
- Scope control: these theorems do not swap `forall k, exists L_k` into one
  language hard for every polynomial exponent. Some proof cases explicitly
  branch on the already-terminal assumption `NP notsubseteq SIZE(poly)`.
