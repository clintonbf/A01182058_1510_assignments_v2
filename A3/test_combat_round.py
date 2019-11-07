import io
from unittest import TestCase
from unittest.mock import patch

from A3 import sud


class TestCombat_round(TestCase):
    @patch('random.randint', side_effect=[20, 1, 20, 10])  # (init, init, attack, dmg_done)
    @patch('random.choice', side_effect=['his skill, cunning and fighting prowess!', 'Zounds! ',
                                         'The life is leaving Superman'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_one_shot(self, mock_output, mock_choice, mock_roll):
        test_p1 = {'Name': 'Batman', 'Class': 'fighter', 'Dexterity': 5, 'HP': {'Current': 10, 'Max': 10},
                   'Attacks': ['a batarang!', 'his skill, cunning and fighting prowess!']}
        test_p2 = {'Name': 'Superman', 'Class': 'warlock', 'Dexterity': 4, 'HP': {'Current': 5, 'Max': 5},
                   'Attacks': ['What does he really have besides his fists?']}

        sud.combat_round(test_p1, test_p2)

        the_output = "The life is leaving Superman\n"
        self.assertIn(the_output, mock_output.getvalue())

    @patch('random.randint', side_effect=[1, 20, 1, 20, 1])  # (init, init, attack, attack, dmg)
    @patch('random.choice', side_effect=['What does he really have besides his fists?', 'A miss!', 'a batarang!',
                                         'A crashing blow! '])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_initiator_misses(self, mock_output, mock_choice, mock_roll):
        test_p1 = {'Name': 'Batman', 'Class': 'fighter', 'Dexterity': 5, 'HP': {'Current': 10, 'Max': 10},
                   'Attacks': ['a batarang!', 'his skill, cunning and fighting prowess!']}
        test_p2 = {'Name': 'Superman', 'Class': 'warlock', 'Dexterity': 4, 'HP': {'Current': 5, 'Max': 5},
                   'Attacks': ['What does he really have besides his fists?']}

        sud.combat_round(test_p1, test_p2)

        self.assertIn("A miss!\n", mock_output.getvalue())

    @patch('random.randint', side_effect=[20, 1, 20, 2, 20, 3])  # (init, init, attack, damage, attack, damage)
    @patch('random.choice', side_effect=['a batarang!', 'Zounds! ', 'What does he really have besides his fists?', 'Wow! '])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_combat_round_riposte(self, mock_output, mock_choice, mock_roll):
        test_p1 = {'Name': 'Batman', 'Class': 'fighter', 'Dexterity': 5, 'HP': {'Current': 10, 'Max': 10},
                   'Attacks': ['a batarang!', 'his skill, cunning and fighting prowess!']}
        test_p2 = {'Name': 'Superman', 'Class': 'warlock', 'Dexterity': 4, 'HP': {'Current': 5, 'Max': 5},
                   'Attacks': ['What does he really have besides his fists?']}

        sud.combat_round(test_p1, test_p2)

        expected_output = ["Zounds! 2 damage done!\n", "Wow! 3 damage done!\n"]
        for output in expected_output:
            self.assertIn(output, mock_output.getvalue())
