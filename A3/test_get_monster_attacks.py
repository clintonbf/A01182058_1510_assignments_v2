from unittest import TestCase

from A3.monster import get_monster_attacks


class TestGet_monster_attacks(TestCase):
    def test_get_monster_attacks_chris(self):
        expected_attacks = ['quiz', 'assignment', 'midterm', 'partner quiz', 'python', 'question when you were trying '
                                                                                       'to hide']

        attacks = get_monster_attacks('Chris')

        for attack in attacks:
            self.assertIn(attack, expected_attacks)

    def test_get_monster_attacks_sam(self):
        expected_attacks = ['quiz', 'assignment', 'midterm', 'comma splice']

        attacks = get_monster_attacks('Sam')

        for attack in attacks:
            self.assertIn(attack, expected_attacks)

    def test_get_monster_attacks_neda(self):
        expected_attacks = ['quiz', 'assignment', 'figma', 'git', 'bootstrap']

        attacks = get_monster_attacks('Neda')

        for attack in attacks:
            self.assertIn(attack, expected_attacks)

    def test_get_monster_attacks_takashi(self):
        expected_attacks = ['quiz', 'assignment', 'midterm', 'miniquiz', 'donut', 'number system']

        attacks = get_monster_attacks('Takashi')

        for attack in attacks:
            self.assertIn(attack, expected_attacks)

    def test_get_monster_attacks_amir(self):
        expected_attacks = ['quiz', 'assignment', 'midterm', 'zombie attack']

        attacks = get_monster_attacks('Amir')

        for attack in attacks:
            self.assertIn(attack, expected_attacks)

