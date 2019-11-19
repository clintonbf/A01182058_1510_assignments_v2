from unittest import TestCase

from A4.question_1 import eliminate_multiples


class TestEliminate_multiples(TestCase):
    def test_eliminate_multiples_no_multiples(self):
        test_list = [3, 5, 7, 9, 11]

        processed_list = eliminate_multiples(test_list, 2)
        self.assertEqual(test_list, processed_list)

    def test_eliminate_multiples_some_multiples(self):
        test_list = [3, 6, 5, 2, 7, 9, 11, 2, 4, 6]
        expected_list = [3, 5, 7, 9, 11]

        self.assertEqual(eliminate_multiples(test_list, 2), expected_list)


