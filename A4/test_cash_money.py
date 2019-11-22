from unittest import TestCase

from A4.question_5 import cash_money


class TestCash_money(TestCase):
    def test_cash_money_raises_error_if_argument_is_not_a_double(self):
        with self.assertRaises(TypeError):
            cash_money(100)

    def test_cash_money_less_than_zero_raises_error(self):
        with self.assertRaises(ValueError):
            cash_money(-1.00)

    # DJE's: all of one type, all of some types
    def test_cash_money_one_hundred(self):
        self.assertDictEqual({100: 1}, cash_money(100.00))

    def test_cash_money_some_denominations_needed(self):
        self.assertDictEqual({50: 1, 10: 1, 5: 1, 1: 1, 0.25: 2, 0.01: 3}, cash_money(66.53))
