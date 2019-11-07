from unittest import TestCase

from A3 import sud


class TestAttempt_attack(TestCase):
    def test_attempt_attack_att_succeed(self):
        self.assertTrue(sud.attempt_attack(5, 4))

    def test_attempt_attack_att_fails(self):
        self.assertFalse(sud.attempt_attack(2, 4))

    def test_attempt_attack_att_eq_dex(self):
        self.assertFalse(sud.attempt_attack(4, 4))
