import unittest

from sliding_window import longest_unique_length, max_window_sum


class UniqueSubstringTests(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(longest_unique_length(""), 0)

    def test_repeated_character(self):
        self.assertEqual(longest_unique_length("aaaa"), 1)

    def test_left_boundary_never_moves_back(self):
        self.assertEqual(longest_unique_length("abba"), 2)

    def test_unicode(self):
        self.assertEqual(longest_unique_length("山a山b"), 3)


class WindowSumTests(unittest.TestCase):
    def test_best_window_at_end(self):
        self.assertEqual(max_window_sum([4, -2, 1, 7], 2), 8)

    def test_all_negative(self):
        self.assertEqual(max_window_sum([-8, -3, -4], 2), -7)

    def test_boundary_widths(self):
        self.assertEqual(max_window_sum([2, -1, 3], 1), 3)
        self.assertEqual(max_window_sum([2, -1, 3], 3), 4)

    def test_invalid_widths(self):
        for values, width in [([], 1), ([1], 0), ([1], -1), ([1], 2)]:
            with self.subTest(values=values, width=width):
                with self.assertRaises(ValueError):
                    max_window_sum(values, width)
