from unittest import TestCase

from A3.constants import get_find_the_stairs_chance


class TestGet_find_the_stairs_chance(TestCase):
    def test_get_find_the_stairs_chance(self):
        self.assertEqual(10, get_find_the_stairs_chance())
