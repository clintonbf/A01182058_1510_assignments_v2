from unittest import TestCase
from unittest.mock import patch

from A3.monster import spawn_monster


class TestSpawn_monster(TestCase):
    @patch('random.choice', side_effect=['Neda'])
    def test_spawn_monster(self, mock_choice):
        expected_m = {'Name': 'Neda', 'HP': {'Current': 5, 'Max': 5}, 'Dexterity': 10, 'Class': 'monster'}

        m = spawn_monster()

        for k in expected_m:
            self.assertEqual(m[k], expected_m[k])
