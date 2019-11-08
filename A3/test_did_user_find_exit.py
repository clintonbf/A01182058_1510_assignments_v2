import io
from unittest import TestCase
from unittest.mock import patch

from A3.sud import did_user_find_exit


class TestDid_user_find_exit(TestCase):
    def test_did_user_find_exit_they_did_not_because_wrong_floor(self):
        self.assertFalse(did_user_find_exit(2, 1, 2, (1, 2)))

    def test_did_user_find_exit_they_did_not_because_wrong_x_coordinate(self):
        self.assertFalse(did_user_find_exit(1, 2, 1, (1, 2)))

    def test_did_user_find_exit_they_did_not_because_wrong_y_coordinate(self):
        self.assertFalse(did_user_find_exit(1, 1, 1, (1, 2)))

    def test_did_user_find_exit_they_did_not_because_floor_and_wrong_y_coordinate(self):
        self.assertFalse(did_user_find_exit(2, 1, 1, (1, 2)))

    def test_did_user_find_exit_they_did_not_because_floor_and_wrong_x_coordinate(self):
        self.assertFalse(did_user_find_exit(2, 2, 2, (1, 2)))

    def test_did_user_find_exit_they_did(self):
        self.assertTrue(did_user_find_exit(1, 1, 2, (1, 2)))

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_did_user_find_exit_they_did_congratulatory_message_is_printed(self, mock_output):
        expected_output = "You managed to find the exit! Enjoy your time off..... you'll be back\n"

        value = did_user_find_exit(1, 1, 2, (1, 2))

        self.assertIn(expected_output, mock_output.getvalue())
