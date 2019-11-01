from unittest import TestCase

import dungeonsanddragons


class TestGenerate_name(TestCase):
    def test_generate_name_correct_length(self):
        test_name = dungeonsanddragons.generate_name(4)

        self.assertEqual(len(test_name), 8)

    def test_evens_are_vowels(self):
        test_name = dungeonsanddragons.generate_name(9)

        for i in range(1, len(test_name), 2):
            self.assertIn(test_name[i], ['a', 'e', 'i', 'o', 'u', 'y'])

    def test_odds_are_consonants(self):
        test_name = dungeonsanddragons.generate_name(9)

        for i in range(0, len(test_name), 2):
            self.assertIn(test_name[i].lower(), ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r',
                                                 's', 't', 'v', 'w', 'x', 'y', 'z'])
