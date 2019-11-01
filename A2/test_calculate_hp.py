from unittest import TestCase
from unittest.mock import patch

import dungeonsanddragons


class TestCalculate_hp(TestCase):

    @patch('random.randint', return_value=6)
    def test_calculate_hp_barbarian(self, mock_roll):

        test_hp = dungeonsanddragons.calculate_hp('barbarian')

        self.assertEqual(test_hp, 6)

    @patch('random.randint', return_value=2)
    def test_calculate_hp_d10_er(self, mock_roll):
        for t_class in ['paladin', 'fighter', 'ranger']:
            test_hp = dungeonsanddragons.calculate_hp(t_class)

            self.assertEqual(test_hp, 2)

    @patch('random.randint', return_value=6)
    def test_calculate_hp_d8_er(self, mock_roll):
        for t_class in ["bard", "cleric", "druid", "monk", "rogue", "warlock"]:
            test_hp = dungeonsanddragons.calculate_hp(t_class)

            self.assertEqual(test_hp, 6)

    @patch('random.randint', return_value=3)
    def test_calculate_hp_d6_er(self, mock_roll):
        for t_class in ["sorcerer", "wizard"]:
            test_hp = dungeonsanddragons.calculate_hp(t_class)

            self.assertEqual(test_hp, 3)
