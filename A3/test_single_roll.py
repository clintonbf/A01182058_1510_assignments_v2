from unittest import TestCase
from unittest.mock import patch

from A3 import sud


class TestSingle_roll(TestCase):

    @patch('random.randint', return_value=5)
    def test_single_roll_6_side(self, mock_sides):
        self.assertEqual(sud.single_roll(mock_sides), 5)
