# MOR08 — inversion complexity in Boolean formulas

Hiroki Morizumi, “A Note on the Inversion Complexity of Boolean Functions in
Boolean Formulas,” CoRR abs/0811.0699 (2008).

- Primary preprint: https://arxiv.org/abs/0811.0699
- Accessed: 2026-08-10
- Consumed claim: for a single-output Boolean function `f`, the minimum
  number of NOT gates in a fan-out-one AND/OR/NOT formula equals its maximum
  number `d(f)` of `1`-to-`0` decreases along an increasing input chain.
- Lower-bound mechanism consumed by LEMMA-156: the paper defines the number
  of NOT gates in the down state, proves that this potential never decreases
  on an increasing input step, and proves that it rises by at least one when
  the formula output falls. The repository derives its own equality case from
  these inequalities; the paper is not cited for a clause-localization
  theorem.
- Scope control: this is a formula theorem. The repository uses it only after
  separately proving that equality in the binary connectivity bound forces
  the relevant circuit output cone to be a formula. It is not applied to
  general DAG circuits.
