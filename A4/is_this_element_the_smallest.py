from unittest import TestCase

from A4.question_4 import is_this_element_the_smallest


class TestIs_this_element_the_smallest(TestCase):
    def test_is_this_element_the_smallest_when_it_is(self):
        self.assertTrue(is_this_element_the_smallest([1, 2, 3, 4, 5], 1))

    def test_is_this_element_the_smallest_when_it_is_not(self):
        self.assertFalse(is_this_element_the_smallest([16, 25, -3, 4, 5], 5))

    def test_is_this_element_the_smallest_when_there_are_duplicates_and_it_is(self):
        self.assertTrue(is_this_element_the_smallest([41, 2, 67, 1, 1], 1))

    def test_is_this_element_the_smallest_when_elements_are_strings(self):
        self.assertTrue(is_this_element_the_smallest(['banana', 'a', 'pear', 'orange'], 'a'))
