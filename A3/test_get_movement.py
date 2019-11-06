from unittest import TestCase
from unittest.mock import patch

from A3.sud import get_movement


class TestGet_movement(TestCase):
    @patch('builtins.input', side_effect=['n'])
    def test_get_movement(self, mock_input):
        direction = get_movement()

        self.assertEqual(direction, 'n')
