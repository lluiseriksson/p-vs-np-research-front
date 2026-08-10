# Cycle 074 local quintet audit

**Label: PROVED** (finite certificate only)

The 94-identifier alphabet obtained by adding identifiers 1,089 and 1,098 was
checked exhaustively for every starting residue and every four-gap tuple in
`{1,...,20}^4`. Each type was tested for all masks 1 through 30 with at most
four nonoverlapping blocks.

| Residue | Types | Failures |
|---:|---:|---:|
| 0 | 160,000 | 540 |
| 1 | 160,000 | 511 |
| 2 | 160,000 | 410 |
| 3 | 160,000 | 326 |
| Total | 640,000 | 1,787 |

The stable representative `(70,71,76,77,80)` omits only mask 8. The original
explicit interval DP independently confirms the bitset result. The audit is
not the full `4*71^4` reduction and is not presented as one; LEMMA-078 needs
only this representative and its translation argument.
