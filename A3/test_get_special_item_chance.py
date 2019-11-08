from unittest import TestCase

from A3.sud import get_special_item_chance


class TestGet_special_item_chance(TestCase):
    def test_get_special_item_chance(self):
        self.assertEqual(15, get_special_item_chance())
