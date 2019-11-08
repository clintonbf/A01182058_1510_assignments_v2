import io
from unittest import TestCase
from unittest.mock import patch

from A3.sud import process_god_mode


class TestProcess_god_mode(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_process_god_mode_god_exit(self, mock_output):
        stats = {'items': False, 'stairs': False, 'escape': (1, 2)}

        expected_output = "The exit is at: (1, 2)\n"
        process_god_mode('god_exit', stats)

        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_process_god_mode_got_battle(self, mock_output):
        expected_output = "God mode activated: Chance of finding special item increased\n"

        stats = {'item': True, 'stairs': False, 'escape': (1, 2)}
        process_god_mode('god_battle', stats)

        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_process_god_mode_got_stairs(self, mock_output):
        expected_output = "God mode activated: Chance of finding stairs increased\n"

        stats = {'item': False, 'stairs': True, 'escape': (1, 2)}
        process_god_mode('god_stairs', stats)

        self.assertEqual(mock_output.getvalue(), expected_output)
