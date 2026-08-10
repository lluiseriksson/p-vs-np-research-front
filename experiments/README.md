# Experiments

`search_literal_subcube.py` is a deterministic finite exhaustive search over
all SAT-gamma formulas using only identifier 1, through a supplied length
bound. Cycle 028 runs it through length 31 to look for equal-length encodings
of `x_1` and `NOT x_1` separated by one bit. The result and exact per-length
counts are stored in `artifacts/literal-subcube-search-31.json` and labeled
`NUMERICAL`.

Any future finite computation is labeled `NUMERICAL`, records its exact input
distribution and random seed, and is barred from supporting an asymptotic
worst-case separation without a separate proof.
