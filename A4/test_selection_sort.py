from unittest import TestCase

from A4.question_4 import selection_sort


class TestSelection_sort(TestCase):
    def test_selection_sort_normal_list(self):
        self.assertEqual([-4, 1, 3, 5, 9], selection_sort([3, 5, 1, 9, -4]))

    def test_selection_sort_already_sorted_list(self):
        self.assertEqual([-4, 1, 3, 5, 9], selection_sort([-4, 1, 3, 5, 9]))

    def test_selection_sort_duplicates_exist(self):
        self.assertEqual([1, 2, 2, 4, 6, 7], selection_sort([4, 1, 2, 6, 7, 2]))

    def test_selection_sort_elements_are_strings(self):
        self.assertEqual(['aardvark', 'apple', 'b', 'b', 'berry', 'cherry'], selection_sort(['cherry', 'b', 'apple',
                                                                                             'berry', 'aardvark', 'b']))

    def test_selection_sort_empty_list_raises_error(self):  # FAILED
        with self.assertRaises(IndexError):
            selection_sort([])

    def test_selection_sort_non_list_raises_error(self):
        with self.assertRaises(TypeError):
            selection_sort('boo')

    def test_selection_non_sortable_list_raises_error(self):
        with self.assertRaises(TypeError):
            selection_sort(['aardvark', True, 'zebra'])

