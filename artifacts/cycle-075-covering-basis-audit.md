# Cycle 075 covering-basis audit

**Label: PROVED** (finite certificates only)

- The deterministic identifier basis contains 318 distinct 15-bit IDs.
- Exhaustive projection checking returns zero failures on all 64,064
  five-column pattern obligations.
- After adjoining the basis to the Cycle-074 alphabet and deduplicating, the
  neutral alphabet has 412 identifiers and maximum block length 68.
- The gap-at-most-20 quintet audit checks 160,000 types per residue and returns
  failure counts `150,134,104,109`, totaling 497.
- Both interval DPs agree that `(70,71,80,85,86)` omits only mask 16.

This artifact does not claim the complete `4*71^4` domain was checked. Its
structural conclusion is narrower: exhaustive free-bit coverage does not
cover the fixed-token and gamma-boundary phases of the neutral block.
