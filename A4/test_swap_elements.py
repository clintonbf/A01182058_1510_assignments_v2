from unittest import TestCase

from A4.question_4 import swap_elements


class TestSwap_elements(TestCase):
    def test_swap_elements(self):
        lst = [1, 2, 3, 4]

        swap_elements(lst, 1, 3)

        self.assertEqual([1, 4, 3, 2], lst)

    # TODO are there other DJEs???