import io
from unittest import TestCase
from unittest.mock import patch

from A3.sud import advise_of_movement_error


class TestAdvise_of_movement_error(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_advise_of_movement_error_invalid_movement(self, mock_output):
        advise_of_movement_error(1)
        expected_output = "Invalid movement option. Please enter again (n, s, w, e)\n"

        self.assertEqual(mock_output.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_advise_of_movement_error_hit_a_wall(self, mock_output):
        advise_of_movement_error(2)
        expected_output = "You hit a wall; ouch. Try a different direction(n, s, w, e)\n"

        self.assertEqual(mock_output.getvalue(), expected_output)
