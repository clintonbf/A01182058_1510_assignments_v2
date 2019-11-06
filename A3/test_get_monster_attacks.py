from unittest import TestCase

from A3.monster import get_monster_attacks


class TestGet_monster_attacks(TestCase):
    def test_get_monster_attacks_chris(self):
        expected_attacks = ['a quiz', 'an assignment', 'the midterm', 'a partner quiz', 'a python',
                            'a question when you were trying to hide']

        attacks = get_monster_attacks('Chris')

        for attack in attacks:
            self.assertIn(attack, expected_attacks)

    def test_get_monster_attacks_sam(self):
        expected_attacks = ['a quiz', 'an assignment', 'the midterm', 'a comma splice']

        attacks = get_monster_attacks('Sam')

        for attack in attacks:
            self.assertIn(attack, expected_attacks)

    def test_get_monster_attacks_neda(self):
        expected_attacks = ['a quiz', 'an assignment', 'figma', 'git', 'bootstrap']

        attacks = get_monster_attacks('Neda')

        for attack in attacks:
            self.assertIn(attack, expected_attacks)

    def test_get_monster_attacks_takashi(self):
        expected_attacks = ['a quiz', 'an assignment', 'the midterm', 'a miniquiz', 'a donut', 'a number system']

        attacks = get_monster_attacks('Takashi')

        for attack in attacks:
            self.assertIn(attack, expected_attacks)

    def test_get_monster_attacks_amir(self):
        expected_attacks = ['a quiz', 'an assignment', 'the midterm', 'a zombie attack', 'a fake quiz']

        attacks = get_monster_attacks('Amir')

        for attack in attacks:
            self.assertIn(attack, expected_attacks)

