from unittest import TestCase

from A4.question_8 import find_max_value_in_a_dictionary


class TestFind_max_value_in_a_dictionary(TestCase):
    def test_find_max_value_in_a_dictionary_when_situation_is_simple(self):
        self.assertEqual(6, find_max_value_in_a_dictionary({3: 6, 4: 5, 1:2, 9: 18, 12: 2}, [3, 4, 1]))

    def test_find_max_value_in_a_dictionary_if_max_exists_twice(self):
        self.assertEqual(6, find_max_value_in_a_dictionary({3: 6, 4: 5, 1: 6, 9: 18, 12: 2}, [3, 4, 1]))

    def test_find_max_value_in_a_dictionary_if_key_not_in_list(self):
        with self.assertRaises(IndexError):
            find_max_value_in_a_dictionary({3: 6, 4: 5, 1: 2, 9: 18, 12: 2}, [10, 17])
