# GKST17 — substitution framework for circuit lower bounds and #SAT

Alexander Golovnev, Alexander Kulikov, Alexander Smal, and Suguru Tamaki,
“Circuit size lower bounds and #SAT upper bounds through a general framework,”
ECCC TR16-022, revision 2, 2017.

- Primary record: https://eccc.weizmann.ac.il/report/2016/022/
- Accessed: 2026-08-10
- Consumed claim: the framework fixes a circuit class, a circuit-complexity
  measure, and allowed substitutions; its main technical input is a case
  analysis proving that some allowed substitution sufficiently reduces the
  measure. For worst/average-case lower bounds, the framework additionally
  requires an explicit disperser/extractor for the induced source class.
- Reported applications: linear average-case bounds for `U_2` and `B_2`
  circuits and faster #SAT algorithms for small linear-size circuits.
- Scope control: the framework does not prove that an ENC-008 conditioned
  prefix decreases unrestricted minimum SAT circuit size, nor does it compare
  the joint semantic quotient with its parent. That is precisely the open
  GATE-004I input, not a consequence of the framework.
