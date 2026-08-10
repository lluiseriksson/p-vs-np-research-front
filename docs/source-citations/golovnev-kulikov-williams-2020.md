# GKW20 — unrestricted-circuit depth reduction

Alexander Golovnev, Alexander Kulikov, and Ryan Williams, “Circuit Depth
Reductions,” ECCC TR18-192, revision 3, 2020.

- Primary record: https://eccc.weizmann.ac.il/report/2018/192/
- Accessed: 2026-08-10
- Consumed claim: every unbounded-depth Boolean circuit of size `s` can be
  represented as an OR of `2^(s/3.9)` width-16 CNFs.
- Source qualification: the paper explicitly says that this structural result
  does not immediately give new lower bounds; its applications depend on
  additional pseudorandom or depth-three lower-bound inputs.
- Scope control: component-count lower bounds for this representation have the
  universal linear ceiling proved in LEMMA-019. The note does not exclude
  arguments exploiting richer structure of the CNF components, but no such
  SAT-specific bridge is claimed here.
