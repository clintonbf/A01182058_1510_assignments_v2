from unittest import TestCase

from A4.question_4 import find_smallest_number_element


class TestFind_smallest_number_element(TestCase):
    def test_find_smallest_number_element_(self):
        test_index = find_smallest_number_element([15, 23, -4, 1])

        self.assertEqual(2, test_index)

    def test_find_smallest_number_element_smallest_at_element_0(self):
        test_index = find_smallest_number_element([0, 1, 2, 3])

        self.assertEqual(0, test_index)

    def test_find_smallest_number_element_duplicate_smallest_element(self):
        test_index = find_smallest_number_element([49, 18, 9, 12, 32, 9, 121, 56])

        self.assertEqual(2, test_index)