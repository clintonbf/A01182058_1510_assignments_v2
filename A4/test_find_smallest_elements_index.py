from unittest import TestCase

from A4.question_4 import find_smallest_elements_index


class TestFind_smallest_elements_index(TestCase):
    def test_find_smallest_elements_index(self):
        test_index = find_smallest_elements_index([15, 23, -4, 1], 0)

        self.assertEqual(2, test_index)

    def test_find_smallest_elements_index_smallest_at_element_0(self):
        test_index = find_smallest_elements_index([0, 1, 2, 3], 0)

        self.assertEqual(0, test_index)

    def test_find_smallest_elements_index_duplicate_smallest_element(self):
        test_index = find_smallest_elements_index([49, 18, 9, 12, 32, 9, 121, 56], 0)

        self.assertEqual(2, test_index)

    def test_find_smallest_elements_index_starting_from_a_higher_index_than_0(self):
        test_index = find_smallest_elements_index([-3, 18, 9, 12, 32, -5, 121, 56], 1)

        self.assertEqual(5, test_index)

    def test_find_smallest_elements_index_when_it_is_at_end(self):
        test_index = find_smallest_elements_index([-3, 18, 9, 12, 32, -5, 121, -56], 0)

        self.assertEqual(7, test_index)

    def test_find_smallest_elements_index_with_strings(self):
        test_index = find_smallest_elements_index(['crumble', 'pie', 'apple', 'strudel'], 0)

        self.assertEqual(2, test_index)