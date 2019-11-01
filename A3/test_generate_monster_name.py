from unittest import TestCase
from unittest.mock import patch

import monster


class TestGenerate_monster_name(TestCase):
    @patch('random.randint', side_effect=[0, 1, 2, 3, 4])
    def test_generate_monster_name(self, mock_roll):
        possible_names = ('Chris', 'Sam', 'Neda', 'Takashi', 'Amir')

        for name in possible_names:
            self.assertEqual(monster.generate_monster_name(), name)
