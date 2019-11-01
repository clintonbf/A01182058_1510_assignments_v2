from unittest import TestCase
from unittest.mock import patch

import dungeonsanddragons


class TestSelect_class(TestCase):

    @patch('builtins.input', side_effect=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    def test_select_class(self, mock_input):
        class_list = ['', 'barbarian', 'bard', 'cleric', 'druid', 'fighter', 'monk', 'paladin', 'ranger', 'rogue',
                      'sorcerer', 'warlock', 'wizard']

        for i in range(1, 12):
            my_class = dungeonsanddragons.select_class()
            self.assertEqual(my_class, class_list[i])
