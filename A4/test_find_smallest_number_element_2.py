from unittest import TestCase

from A4.question_4 import find_smallest_number_element_2


class TestFind_smallest_number_element_2(TestCase):
    def test_find_smallest_number_element(self):
        test_index = find_smallest_number_element_2([15, 23, -4, 1], 0)

        self.assertEqual(2, test_index)

    def test_find_smallest_number_element_smallest_at_element_0(self):
        test_index = find_smallest_number_element_2([0, 1, 2, 3], 0)

        self.assertEqual(0, test_index)

    def test_find_smallest_number_element_duplicate_smallest_element(self):
        test_index = find_smallest_number_element_2([49, 18, 9, 12, 32, 9, 121, 56], 0)

        self.assertEqual(2, test_index)

    def test_find_smallest_number_element_starting_from_a_higher_index_than_0(self):
        test_index = find_smallest_number_element_2([-3, 18, 9, 12, 32, -5, 121, 56], 1)

        self.assertEqual(5, test_index)
