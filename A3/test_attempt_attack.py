from unittest import TestCase

import A3.combat
from A3 import sud


class TestAttempt_attack(TestCase):
    def test_attempt_attack_att_succeed(self):
        self.assertTrue(A3.combat.attempt_attack(5, 4))

    def test_attempt_attack_att_fails(self):
        self.assertFalse(A3.combat.attempt_attack(2, 4))

    def test_attempt_attack_att_eq_dex(self):
        self.assertFalse(A3.combat.attempt_attack(4, 4))
