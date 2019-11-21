from unittest import TestCase

from A4.question_4 import selection_sort


class TestSelection_sort(TestCase):
    def test_selection_sort_normal_list(self):

        self.assertEqual([-4, 1, 3, 5, 9], selection_sort([3, 5, 1, 9, -4]))
