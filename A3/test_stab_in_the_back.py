from unittest import TestCase
from unittest.mock import patch

from A3.sud import stab_in_the_back


class TestStab_in_the_back(TestCase):
    @patch('random.randint', side_effect=[1])
    def test_stab_in_the_back_successful_attack(self, mock_roll):
        self.assertTrue(stab_in_the_back())

    @patch('random.randint', side_effect=[2, 3, 4, 5, 6, 7, 8, 9, 10])
    def test_stab_in_the_back_unsuccessful_attack(self, mock_roll):

        for i in range(2, 11):
            self.assertFalse(stab_in_the_back())

