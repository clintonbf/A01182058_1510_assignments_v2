from unittest import TestCase

from A3.sud import get_valid_movement_choices


class TestGet_valid_movement_choices(TestCase):
    def test_get_valid_movement_choices(self):
        choices_to_check = ('n', 's', 'w', 'e', 'god_battle', 'god_stairs', 'god_exit')

        self.assertEqual(choices_to_check, get_valid_movement_choices())
