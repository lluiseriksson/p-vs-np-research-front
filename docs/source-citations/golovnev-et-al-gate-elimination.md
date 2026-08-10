# GHKK16 — limits of gate elimination

Alexander Golovnev, Edward A. Hirsch, Alexander Knop, and Alexander S. Kulikov,
“On the Limits of Gate Elimination,” MFCS 2016, LIPIcs 58, 46:1–46:13.

- DOI: https://doi.org/10.4230/LIPIcs.MFCS.2016.46
- Primary PDF: https://golovnev.org/papers/limits.pdf
- Accessed: 2026-08-10
- Consumed claim: the standard generic gate-elimination framework, with an
  induction step certified for all functions/circuits using a fixed number of
  substitutions, cannot exceed a constant-times-`n` lower bound; the constant
  depends on the local substitution budget.
- Scope control: this is a limitation of a formalized method, not a theorem
  that superlinear unrestricted-circuit lower bounds are false. The source
  explicitly notes that target-family-specific induction steps are logically
  possible and are not all captured by the generic construction.
