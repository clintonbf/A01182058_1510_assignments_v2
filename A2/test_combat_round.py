import io
from unittest import TestCase
from unittest.mock import patch

import dungeonsanddragons


class TestCombat_round(TestCase):
    @patch('random.randint', side_effect=[20, 1, 20, 10])  # (init, init, attack, dmg_done)
    @patch('random.choice', side_effect=['Zounds! ', 'The life is leaving Superman'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_one_shot(self, mock_output, mock_choice, mock_roll):
        test_p1 = {'Name': 'Batman', 'Class': 'fighter', 'Dexterity': 5, 'HP': {'Current': 10, 'Max': 10}}
        test_p2 = {'Name': 'Superman', 'Class': 'warlock', 'Dexterity': 4, 'HP': {'Current': 5, 'Max': 5}}

        dungeonsanddragons.combat_round(test_p1, test_p2)

        expected_output = ["Batman attacks first!\n", "Batman attacks!\n", "Zounds! 10 damage done!\n",
                           "The life is leaving Superman\n"]

        the_output = expected_output[0] + expected_output[1] + expected_output[2] + expected_output[3]

        self.assertEqual(the_output, mock_output.getvalue())

    @patch('random.randint', side_effect=[1, 20, 1, 20, 1])  # (init, init, attack, attack, dmg)
    @patch('random.choice', side_effect=['A miss!', 'A crashing blow! '])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_initiator_misses(self, mock_output, mock_choice, mock_roll):
        test_p1 = {'Name': 'Batman', 'Class': 'fighter', 'Dexterity': 5, 'HP': {'Current': 10, 'Max': 10}}
        test_p2 = {'Name': 'Superman', 'Class': 'warlock', 'Dexterity': 4, 'HP': {'Current': 5, 'Max': 5}}

        dungeonsanddragons.combat_round(test_p1, test_p2)

        expected_output = ["Superman attacks first!\n", "Superman attacks!\n", "A miss!\n",
                           "Batman attacks!\n", "A crashing blow! 1 damage done!\n"]

        the_output = expected_output[0] + expected_output[1] + expected_output[2] + expected_output[3] \
                     + expected_output[4]

        self.assertEqual(the_output, mock_output.getvalue())

    @patch('random.randint', side_effect=[20, 1, 20, 2, 20, 3])  # (init, init, attack, damage, attack, damage)
    @patch('random.choice', side_effect=['Zounds! ', 'Wow! '])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_riposte(self, mock_output, mock_choice, mock_roll):
        test_p1 = {'Name': 'Batman', 'Class': 'fighter', 'Dexterity': 5, 'HP': {'Current': 10, 'Max': 10}}
        test_p2 = {'Name': 'Superman', 'Class': 'warlock', 'Dexterity': 4, 'HP': {'Current': 5, 'Max': 5}}

        dungeonsanddragons.combat_round(test_p1, test_p2)

        expected_output = ["Batman attacks first!\n", "Batman attacks!\n", "Zounds! 2 damage done!\n",
                           "Superman attacks!\n", "Wow! 3 damage done!\n"]

        the_output = expected_output[0] + expected_output[1] + expected_output[2] + expected_output[3] + expected_output[4]

        self.assertEqual(the_output, mock_output.getvalue())
