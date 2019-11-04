from unittest import TestCase
from unittest.mock import patch

from A3 import monster


class TestGenerate_monster_name(TestCase):
    @patch('random.choice', side_effect=['Chris', 'Sam', 'Neda', 'Takashi', 'Amir'])
    def test_generate_monster_name(self, mock_roll):
        possible_names = ('Chris', 'Sam', 'Neda', 'Takashi', 'Amir')

        for name in possible_names:
            self.assertEqual(monster.generate_monster_name(), name)
