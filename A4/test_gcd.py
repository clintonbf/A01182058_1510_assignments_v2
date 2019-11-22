from unittest import TestCase

from A4.question_2 import gcd


class TestGcd(TestCase):
    def test_gcd_a_is_greater_than_b(self):
        self.assertEqual(6, gcd(270, 192))

    def test_gcd_b_is_greater_than_a(self):
        self.assertEqual(6, gcd(192, 270))

    def test_gcd_a_is_not_an_integer(self):
        with self.assertRaises(TypeError):
            gcd('boo', 5)

    def test_gcd_b_is_not_an_integer(self):
        with self.assertRaises(TypeError):
            gcd(5, 'boo')

    def test_gcd_a_and_b_are_not_integers(self):
        with self.assertRaises(TypeError):
            gcd('foo', 'boo')

    def test_gcd_a_is_zero(self):
        with self.assertRaises(ValueError):
            gcd(0, 5)

    def test_gcd_b_is_zero(self):
        with self.assertRaises(ValueError):
            gcd(5, 0)

    def test_gcd_a_and_b_are_zero(self):
        with self.assertRaises(ValueError):
            gcd(0, 0)

