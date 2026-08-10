# FIS75 — size-efficient negation normalization

Michael J. Fischer, “The Complexity of Negation-Limited Networks — A Brief
Survey,” *Automata Theory and Formal Languages*, LNCS 33, 71–82 (1975).

- Primary technical report: https://publications.csail.mit.edu/lcs/pubs/pdf/MIT-LCS-TM-065.pdf
- Bibliographic record: https://dblp.org/rec/conf/automata/Fischer75
- Accessed: 2026-08-11
- Consumed claim: the negation-limited network transformation preserves
  polynomial size while reducing a polynomial-size Boolean circuit on `n`
  variables to at most `ceil(log_2(n+1))` negations; HLS10 explicitly
  restates this Fischer consequence in its primary introduction.
- Scope control: polynomial overhead is far too coarse for the exact linear
  identity sought in GATE-004AH. The theorem blocks any inference that a low
  NOT count alone forces superpolynomial size, but it neither supplies nor
  refutes the required fine-grained binary/NOT tradeoff.
