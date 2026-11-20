import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from main import find_first_extremes, sum_negatives_between


class TestExtremes(unittest.TestCase):
    def test_example(self):
        values = [5, -3, -7, 2, 8, -1, 4, -9, 6, 0]
        total, max_i, min_i, left, right = sum_negatives_between(values)
        self.assertEqual((max_i, min_i), (4, 7))
        self.assertEqual((left, right), (4, 7))
        self.assertEqual(total, -1)

    def test_positive_array(self):
        self.assertEqual(sum_negatives_between([1, 2, 3])[0], 0)

    def test_all_negative(self):
        self.assertEqual(sum_negatives_between([-1, -2, -3])[0], -2)

    def test_all_equal(self):
        self.assertEqual(sum_negatives_between([4, 4, 4])[0], 0)

    def test_adjacent_extremes(self):
        self.assertEqual(sum_negatives_between([3, -1, 5])[0], 0)

    def test_negative_sum_after_max(self):
        self.assertEqual(sum_negatives_between([2, -10, -1, -2, 5])[0], -3)

    def test_first_maximum_is_used(self):
        values = [5, 1, 5, -2, 1]
        max_i, min_i = find_first_extremes(values)
        self.assertEqual((max_i, min_i), (0, 3))
        self.assertEqual(sum_negatives_between(values)[0], 0)

    def test_first_minimum_is_used(self):
        values = [0, -2, 3, -2, -5]
        max_i, min_i = find_first_extremes(values)
        self.assertEqual((max_i, min_i), (2, 4))
        self.assertEqual(sum_negatives_between(values)[0], -2)

    def test_single_element(self):
        self.assertEqual(sum_negatives_between([7])[0], 0)

    def test_empty_array(self):
        with self.assertRaises(ValueError):
            find_first_extremes([])


if __name__ == "__main__":
    unittest.main()
