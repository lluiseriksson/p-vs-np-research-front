from __future__ import annotations

import itertools
import unittest

from affine_index_extension import affine_index_extension, depth_bound, gate_bound


class AffineIndexExtensionTests(unittest.TestCase):
    def test_small_total_extension(self) -> None:
        identifiers = (4, 5, 6)
        rows = {
            (4, False): "0000",
            (4, True): "0001",
            (5, False): "0110",
            (5, True): "0111",
            (6, False): "1100",
            (6, True): "1110",
        }
        base = "10100101"
        directions = {
            4: "11000000",
            5: "00010100",
            6: "00000011",
        }
        circuit = affine_index_extension(rows, base, directions)
        self.assertEqual(len(circuit.gates), gate_bound(3, 4))
        self.assertEqual(gate_bound(3, 4), 36)
        self.assertEqual(depth_bound(3, 4), 7)
        self.assertLessEqual(circuit.depth(), depth_bound(3, 4))

        def xor(*words: str) -> str:
            return "".join(
                str(sum(int(word[index]) for word in words) % 2)
                for index in range(len(words[0]))
            )

        for assignment in itertools.product((False, True), repeat=3):
            selected = [
                directions[identifier]
                for identifier, value in zip(identifiers, assignment)
                if value
            ]
            suffix = xor(base, *selected) if selected else base
            for identifier_index, identifier in enumerate(identifiers):
                for polarity in (False, True):
                    bits = tuple(
                        bit == "1" for bit in rows[(identifier, polarity)] + suffix
                    )
                    self.assertEqual(
                        circuit.evaluate(bits), polarity == assignment[identifier_index]
                    )

        unused_prefix = "1010"
        self.assertNotIn(unused_prefix, rows.values())
        for suffix in itertools.product((False, True), repeat=len(base)):
            bits = tuple(bit == "1" for bit in unused_prefix) + suffix
            self.assertFalse(circuit.evaluate(bits))

    def test_invalid_overlap_is_rejected(self) -> None:
        rows = {(1, False): "00", (1, True): "01", (2, False): "10", (2, True): "11"}
        with self.assertRaises(ValueError):
            affine_index_extension(
                rows,
                "000",
                {1: "110", 2: "011"},
            )


if __name__ == "__main__":
    unittest.main()
