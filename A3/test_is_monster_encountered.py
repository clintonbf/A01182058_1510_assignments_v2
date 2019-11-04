from unittest import TestCase
from unittest.mock import patch

from A3 import sud


class TestIs_monster_encountered(TestCase):
    @patch('random.randint', return_value=1)
    def test_is_monster_encountered_yes(self, mock_roll):
        self.assertTrue(sud.is_monster_encountered())

    @patch('random.randint', side_effect=[2, 3, 4])
    def test_is_monster_encountered_no(self, mock_roll):

        for i in range(3):
            self.assertFalse(sud.is_monster_encountered())
