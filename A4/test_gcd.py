from unittest import TestCase

from A4.question_2 import gcd


class TestGcd(TestCase):
    def test_gcd_non_zero_integer_passed(self):
        self.fail()

    def test_gcd_a_is_greater_than_b(self):
        self.assertEqual(6, gcd(270, 192))

    def test_gcd_b_is_greater_than_a(self):
        self.assertEqual(6, gcd(192, 270))

    def test_gcd_zero_is_passed(self):
        self.assertEqual(0, gcd(0, 192))

    def test_gcd_2_zeroes_are_passed(self):
        self.assertEqual(0, gcd(0, 0))

