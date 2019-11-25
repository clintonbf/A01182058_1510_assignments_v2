from unittest import TestCase

from A4.question_8 import find_first_key_of_a_value


class TestFind_first_key_of_a_value(TestCase):
    def test_find_first_key_of_a_value_error_raise_if_value_doesnt_exist(self):
        with self.assertRaises(IndexError):
            find_first_key_of_a_value(18, {'apple': 5, 'cherry': 1, 'koala': 5, 'rhubarb': 7})

    def test_find_first_key_of_a_value_value_exists_once(self):
        self.assertEqual('cherry', find_first_key_of_a_value(1, {'apple': 5, 'cherry': 1, 'koala': 5, 'rhubarb': 7}))

    def test_find_first_key_of_a_value_value_exists_multiple_times(self):
        self.assertEqual('cherry', find_first_key_of_a_value(1, {'apple': 5, 'cherry': 1, 'koala': 1, 'rhubarb': 7}))
