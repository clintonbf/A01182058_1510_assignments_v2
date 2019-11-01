from unittest import TestCase

import dungeonsanddragons


class TestGenerate_vowel(TestCase):
    def test_generate_vowel(self):
        my_vowel = dungeonsanddragons.generate_vowel()

        self.assertIn(my_vowel, ['a', 'e', 'i', 'o', 'u', 'y'])
