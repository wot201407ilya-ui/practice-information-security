import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from greedy import greedy_strength
from main import max_strength


class TestGreedy(unittest.TestCase):
    def test_matches_dp_for_all_values(self):
        for heads in range(1, 100):
            with self.subTest(heads=heads):
                self.assertEqual(
                    greedy_strength(heads)[0],
                    max_strength(heads)[0],
                )

    def test_greedy_decomposition_is_valid(self):
        for heads in range(1, 100):
            strength, parts = greedy_strength(heads)
            with self.subTest(heads=heads):
                self.assertEqual(sum(parts), heads)
                self.assertTrue(all(1 <= part <= 7 for part in parts))
                product = 1
                for part in parts:
                    product *= part
                self.assertEqual(product, strength)

    def test_invalid_input(self):
        for heads in (0, -1, 100):
            with self.subTest(heads=heads):
                with self.assertRaises(ValueError):
                    greedy_strength(heads)


if __name__ == "__main__":
    unittest.main()
