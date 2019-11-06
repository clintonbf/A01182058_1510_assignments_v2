from unittest import TestCase
from unittest.mock import patch

from A2.dungeonsanddragons import choose_attack


class TestChoose_attack(TestCase):
    @patch('random.choice', side_effect=['kitty', 'puppy', 'otter', 'longsword', 'AK-47', 'thermonuclear device'])
    def test_choose_monster_attack(self, mock_choice):
        attacks = ['kitty', 'puppy', 'otter', 'longsword', 'AK-47', 'thermonuclear device']

        for attack in attacks:
            self.assertEqual(choose_attack(attacks), attack)
