from unittest import TestCase

import dungeonsanddragons


class TestGenerate_syllable(TestCase):
    def test_generate_syllable_first_char_is_consonant(self):
        my_syllable = dungeonsanddragons.generate_syllable()

        self.assertIn(my_syllable[0], ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't',
                                       'v', 'w', 'x', 'y', 'z'])

    def test_generate_syllable_char_2_is_vowel(self):
        my_syllable = dungeonsanddragons.generate_syllable()

        self.assertIn(my_syllable[1], ['a', 'e', 'i', 'o', 'u', 'y'])

    def test_generate_syllable_is_2_char_long(self):
        my_syllable = dungeonsanddragons.generate_syllable()

        self.assertEqual(len(my_syllable), 2)
