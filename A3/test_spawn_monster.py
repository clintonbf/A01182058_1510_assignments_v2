from unittest import TestCase

from A3.monster import spawn_monster


class TestSpawn_monster(TestCase):
    def test_spawn_monster(self):
        expected_m = {'Name': 'Neda', 'HP': {'Current': 5, 'Max': 5}, 'Dexterity': 0, 'Class': 'monster'}

        m = spawn_monster()

        for k in expected_m():
            self.assertEqual(m[k], expected_m[k])
