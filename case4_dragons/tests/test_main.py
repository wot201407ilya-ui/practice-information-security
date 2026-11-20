import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import max_strength


class TestDragonStrength(unittest.TestCase):
    def test_known_values(self):
        expected = {
            1: (1, [1]),
            2: (2, [2]),
            3: (3, [3]),
            4: (4, [4]),
            5: (6, [3, 2]),
            6: (9, [3, 3]),
            7: (12, [4, 3]),
            8: (18, [3, 3, 2]),
            9: (27, [3, 3, 3]),
            10: (36, [4, 3, 3]),
            11: (54, [3, 3, 3, 2]),
            12: (81, [3, 3, 3, 3]),
            13: (108, [4, 3, 3, 3]),
            20: (1458, [3, 3, 3, 3, 3, 3, 2]),
            30: (59049, [3] * 10),
            50: (86093442, [3] * 16 + [2]),
            99: (3 ** 33, [3] * 33),
        }

        for heads, (strength, parts) in expected.items():
            with self.subTest(heads=heads):
                self.assertEqual(max_strength(heads), (strength, parts))

    def test_every_value_has_valid_decomposition(self):
        for heads in range(1, 100):
            strength, parts = max_strength(heads)
            with self.subTest(heads=heads):
                self.assertEqual(sum(parts), heads)
                self.assertTrue(all(1 <= part <= 7 for part in parts))
                product = 1
                for part in parts:
                    product *= part
                self.assertEqual(product, strength)

    def test_invalid_input(self):
        for heads in (0, -1, 100, 1000):
            with self.subTest(heads=heads):
                with self.assertRaises(ValueError):
                    max_strength(heads)


if __name__ == "__main__":
    unittest.main()
