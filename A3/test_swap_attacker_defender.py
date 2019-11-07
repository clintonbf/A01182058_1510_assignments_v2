from unittest import TestCase

from A3.sud import swap_attacker_defender


class TestSwap_attacker_defender(TestCase):
    def test_swap_attacker_defender_attacker_becomes_defender(self):
        r = {'attacker': 0, 'defender': 1}

        swap_attacker_defender(r)
        self.assertEqual(r['attacker'], 1)

    def test_swap_attacker_defender_defender_becomes_attacker(self):
        r = {'attacker': 1, 'defender': 0}

        swap_attacker_defender(r)
        self.assertEqual(r['attacker'], 0)