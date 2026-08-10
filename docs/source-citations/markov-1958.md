# MAR58 — inversion complexity by decreases on increasing chains

A. A. Markov, “On the Inversion Complexity of a System of Functions,”
*Journal of the ACM* 5(4), 331–334 (1958), translated by Morris D. Friedman.

- Primary DOI: https://doi.org/10.1145/320941.320945
- Original Russian paper: https://www.mathnet.ru/eng/dan22436
- Accessed: 2026-08-10
- Consumed claim: if `d(f)` is the maximum number of `1`-to-`0` decreases of
  a Boolean function along an increasing input chain, the minimum number of
  NOT gates in an AND/OR/NOT circuit for `f` is
  `ceil(log_2(d(f)+1))`.
- Scope control: this counts NOT gates only. It does not give total circuit
  size, add across disjoint components, or establish the implication-tail
  direct-sum theorem required by GATE-004W.
