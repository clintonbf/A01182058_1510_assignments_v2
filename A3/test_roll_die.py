from unittest import TestCase
from unittest.mock import patch

import A3.combat
from A3 import sud


class TestRoll_die(TestCase):
    def test_roll_die_0_rolls(self):
        self.assertEqual(A3.combat.roll_die(0, 5), 0)

    def test_roll_die_0_sided_die(self):
        self.assertEqual(A3.combat.roll_die(5, 0), 0)

    @patch('random.randint', return_value=3)
    def test_roll_1_rolls_of_6(self, mock_roll):
        self.assertEqual(A3.combat.roll_die(1, 6), 3)

    @patch('random.randint', side_effect=[4, 4])
    def test_roll_2_rolls_of_6(self, mock_roll):
        self.assertEqual(A3.combat.roll_die(2, 6), 8)

    @patch('random.randint', side_effect=[1, 6, 4])
    def test_roll_3_rolls_of_6(self, mock_roll):
        self.assertEqual(A3.combat.roll_die(3, 6), 11)
