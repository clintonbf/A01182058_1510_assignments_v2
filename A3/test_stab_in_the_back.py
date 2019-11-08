from unittest import TestCase
from unittest.mock import patch

from A3.sud import stab_in_the_back


class TestStab_in_the_back(TestCase):
    @patch('random.randint', side_effect=[2])
    def test_stab_in_the_back_successful_attack_does_2_dmg(self, mock_roll):
        self.assertTrue(stab_in_the_back(1), 2)

    def test_stab_in_the_back_unsuccessful_attack(self):
        self.assertEqual(stab_in_the_back(2), 0)
