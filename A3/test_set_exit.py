from unittest import TestCase
from unittest.mock import patch

from A3.sud import set_exit
from A3.constants import get_max_x, get_max_y, get_min_x, get_min_y


class TestSet_exit(TestCase):
    @patch('random.choice', side_effect=['x', 3])
    @patch('random.randint', side_effect=[get_min_x()])
    def test_set_exit_when_wall_is_min_x(self, mock_specific, mock_choice):
        the_exit = set_exit()

        self.assertEqual(the_exit, (get_min_x(), 3))

    @patch('random.choice', side_effect=['x', 3])
    @patch('random.randint', side_effect=[get_max_x()])
    def test_set_exit_when_wall_is_max_x(self, mock_specific, mock_choice):
        the_exit = set_exit()

        self.assertEqual(the_exit, (get_max_x(), 3))

    @patch('random.choice', side_effect=['y', 3])
    @patch('random.randint', side_effect=[get_min_y()])
    def test_set_exit_when_wall_is_min_y(self, mock_specific, mock_choice):
        the_exit = set_exit()

        self.assertEqual(the_exit, (3, get_min_y()))

    @patch('random.choice', side_effect=['y', 3])
    @patch('random.randint', side_effect=[get_max_y()])
    def test_set_exit_when_wall_is_max_y(self, mock_specific, mock_choice):
        the_exit = set_exit()

        self.assertEqual(the_exit, (3, get_max_y()))
