from unittest import TestCase

from A4.question_1 import generate_multiples


class TestGenerate_multiples(TestCase):
    def test_generate_multiples_no_multiple(self):
        self.assertEqual(generate_multiples(6, 10), [])

    def test_generate_multiples_one_multiple(self):
        self.assertEqual(generate_multiples(6, 12), [12])

    def test_generate_multiples_some_multiples(self):
        self.assertEqual(generate_multiples(2, 10), [4, 6, 8, 10])

