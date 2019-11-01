from unittest import TestCase
from unittest.mock import patch

from dungeonsanddragons import create_character


class TestCreate_character(TestCase):
    @patch('builtins.input', side_effect=[1, 2, 2, 2, 3, 2, 4, 2, 5, 2, 6, 2, 7, 2, 8, 2, 9, 2])
    def test_create_character_race(self, mock_input):

        race_list = ['', 'dragonborn', 'dwarf', 'elf', 'gnome', 'half-elf', 'halfling', 'half-orc', 'human', 'tiefling']

        for i in range(1, len(race_list)):
            my_char = create_character(4)
            self.assertEqual(my_char['Race'], race_list[i])

    @patch('builtins.input', side_effect=[4, 1, 4, 2, 4, 3, 4, 4, 4, 5, 4, 6, 4, 7, 4, 8, 4, 9, 4, 10, 4, 11, 4, 12])
    def test_create_character_class(self, mock_input):
        class_list = ['', 'barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue',
                      'sorcerer', 'warlock', 'wizard']

        for i in range(1, len(class_list)):
            my_char = create_character(4)
            self.assertEqual(my_char['Class'], class_list[i])

    @patch('builtins.input', side_effect=[1, 2])  # class = bard, race = halfling
    @patch('dungeonsanddragons.calculate_hp', return_value=8)
    def test_character_hp(self, mock_input, mock_roll):
        my_char = create_character(4)

        self.assertEqual((my_char['HP']['Max']), 8)

    @patch('builtins.input', side_effect=[1, 2])
    @patch('dungeonsanddragons.roll_die', side_effect=[3, 3, 3, 3, 3, 3, 3])
    def test_create_character_list_attributes_min(self, mock_input, mock_roll):
        my_char = create_character(3)

        att_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

        for i in range(0, len(att_list)):
            self.assertEqual(my_char[att_list[i]], 3)

    @patch('builtins.input', side_effect=[1, 2])
    @patch('dungeonsanddragons.roll_die', side_effect=[18, 18, 18, 18, 18, 18, 18])
    def test_create_character_list_attributes_max(self, mock_input, mock_roll):
        my_char = create_character(3)

        att_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

        for i in range(0, len(att_list)):
            self.assertEqual(my_char[att_list[i]], 18)

    @patch('builtins.input', side_effect=[1, 2])
    @patch('dungeonsanddragons.roll_die', side_effect=[9, 9, 9, 9, 9, 9, 9])
    def test_create_character_list_attributes_max(self, mock_input, mock_roll):
        my_char = create_character(3)

        att_list = ["Strength", "Dexterity", "Constitution", "Intelligence", "Wisdom", "Charisma"]

        for i in range(0, len(att_list)):
            self.assertEqual(my_char[att_list[i]], 9)

    @patch('builtins.input', side_effect=[1, 2])
    def test_create_character_no_xp(self, mock_input):
        my_char = create_character(4)

        self.assertEqual(my_char['XP'], 0)

    @patch('builtins.input', side_effect=[1, 2])
    def test_create_character_no_inv(self, mock_input):
        my_char = create_character(4)

        self.assertEqual(len(my_char['Inventory']), 0)
