from unittest import TestCase
from unittest.mock import patch

import A3.combat


class TestCalculate_dmg(TestCase):

    @patch('random.randint', side_effect=[3, 3])
    def test_calculate_dmg_for_successful_attack(self, mock_roll):
        test_hp = A3.combat.calculate_dmg(True)
        self.assertEqual(test_hp, 3)

    def test_calculate_dmg_when_no_hit(self):
        test_hp = A3.combat.calculate_dmg(False)
        self.assertEqual(test_hp, 0)
