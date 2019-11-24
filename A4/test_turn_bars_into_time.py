from unittest import TestCase

from A4.question_8 import turn_bars_into_time


class TestTurn_bars_into_time(TestCase):
    def test_turn_bars_into_time_numbers_supplied(self):
        self.assertEqual("10:59", turn_bars_into_time([1, 3, 2, 4], {1: 1, 5: 2, 0: 3, 9: 4}))
