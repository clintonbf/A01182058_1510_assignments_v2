from unittest import TestCase
from unittest.mock import patch

from A3.sud import process_cheap_shot


class TestProcess_cheap_shot(TestCase):
    @patch('random.randint', side_effect=[1, 1])
    def test_process_cheap_shot_damage_done(self, mock_roll):
        damage = process_cheap_shot()

        self.assertEqual(damage, 1)

    @patch('random.randint', side_effect=[10])
    def test_process_cheap_shot_no_damage_done(self, mock_roll):
        damage = process_cheap_shot()

        self.assertEqual(damage, 0)
