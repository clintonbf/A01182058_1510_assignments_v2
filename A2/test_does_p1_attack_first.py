from unittest import TestCase
from unittest.mock import patch

import dungeonsanddragons


class TestDoes_p1_attack_first(TestCase):
    @patch('random.randint', side_effect=[4, 6])
    def test_does_p1_attack_first_no(self, mock_roll):

        self.assertFalse(dungeonsanddragons.does_p1_attack_first())

    @patch('random.randint', side_effect=[10, 6])
    def test_does_p1_attack_first_yes(self, mock_roll):
        self.assertTrue(dungeonsanddragons.does_p1_attack_first())

    @patch('random.randint', side_effect=[10, 10, 10, 6])
    def test_does_p1_attack_first_will_loop(self, mock_roll):
        self.assertTrue(dungeonsanddragons.does_p1_attack_first())