from unittest import TestCase
from unittest.mock import patch

import dungeonsanddragons


class TestSelect_race(TestCase):

    @patch('builtins.input', side_effect=[1, 2, 3, 4, 5, 6, 7, 8, 9])
    def test_select_race(self, mock_input):
        race_list = ['', 'dragonborn', 'dwarf', 'elf', 'gnome', 'half-elf', 'halfling', 'half-orc', 'human', 'tiefling']

        for i in range(1, 9):
            my_race = dungeonsanddragons.select_race()
            self.assertEqual(my_race, race_list[i])
