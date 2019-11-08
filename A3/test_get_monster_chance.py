from unittest import TestCase

from A3.sud import get_monster_chance


class TestGet_monster_chance(TestCase):
    def test_get_monster_chance(self):
        self.assertEqual(4, get_monster_chance())
