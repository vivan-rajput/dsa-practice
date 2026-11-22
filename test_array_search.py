import unittest

from array_search import first_occurrence, two_sum


class FirstOccurrenceTests(unittest.TestCase):
    def test_returns_leftmost_duplicate(self):
        self.assertEqual(first_occurrence([1, 4, 4, 4, 9], 4), 1)

    def test_missing_targets(self):
        for target in (0, 3, 10):
            with self.subTest(target=target):
                self.assertIsNone(first_occurrence([1, 4, 9], target))

    def test_empty(self):
        self.assertIsNone(first_occurrence([], 1))

    def test_single_element(self):
        self.assertEqual(first_occurrence([3], 3), 0)


class TwoSumTests(unittest.TestCase):
    def test_negatives(self):
        self.assertEqual(two_sum([-3, 7, 1], 4), (0, 1))

    def test_duplicate_values_can_pair(self):
        self.assertEqual(two_sum([3, 3], 6), (0, 1))

    def test_cannot_reuse_an_index(self):
        self.assertIsNone(two_sum([3], 6))

    def test_earliest_matching_indices(self):
        self.assertEqual(two_sum([2, 2, 5, 5], 7), (0, 2))
