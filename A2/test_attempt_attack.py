from unittest import TestCase

import dungeonsanddragons


class TestAttempt_attack(TestCase):
    def test_attempt_attack_att_succeed(self):
        self.assertTrue(dungeonsanddragons.attempt_attack(5, 4))

    def test_attempt_attack_att_fails(self):
        self.assertFalse(dungeonsanddragons.attempt_attack(2, 4))

    def test_attempt_attack_att_eq_dex(self):
        self.assertFalse(dungeonsanddragons.attempt_attack(4, 4))
