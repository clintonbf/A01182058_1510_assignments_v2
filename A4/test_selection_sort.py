from unittest import TestCase

from A4.question_4 import selection_sort


class TestSelection_sort(TestCase):
    def test_selection_sort_normal_list(self):
        self.assertEqual([-4, 1, 3, 5, 9], selection_sort([3, 5, 1, 9, -4]))

    def test_selection_sort_already_sorted_list(self):
        self.assertEqual([-4, 1, 3, 5, 9], selection_sort([-4, 1, 3, 5, 9]))

    def test_selection_sort_duplicates_exist(self):
        self.assertEqual([1, 2, 2, 4, 6, 7], selection_sort([4, 1, 2, 6, 7, 2]))
