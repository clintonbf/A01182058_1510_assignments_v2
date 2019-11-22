from unittest import TestCase

from A4.question_1 import eratosthenes


class TestEratosthenes(TestCase):
    def test_eratosthenes_upper_bound_is_below_0(self):
        with self.assertRaises(ValueError):
            eratosthenes(-1)

    def test_eratosthenes_upper_bound_is_0(self):
        self.assertEqual([], eratosthenes(0))

    def test_eratosthenes_upper_bound_is_one(self):
        self.assertEqual([], eratosthenes(1))

    def test_eratosthenes_upper_bound_is_greater_than_1(self):
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 19, 23, 29], eratosthenes(30))

