from unittest import TestCase

from A3.constants import get_extra_commands


class TestGet_extra_commands(TestCase):
    def test_get_extra_commands_test_all_commands(self):
        expected_commands = ('help', 'god_exit', 'god_battle', 'god_stairs')

        for i in range(len(expected_commands)):
            self.assertEqual(get_extra_commands()[i], expected_commands[i])
