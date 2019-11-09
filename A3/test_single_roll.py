from unittest import TestCase
from unittest.mock import patch

import A3.combat


class TestSingle_roll(TestCase):

    @patch('random.randint', return_value=5)
    def test_single_roll_6_side(self, mock_sides):
        self.assertEqual(A3.combat.single_roll(mock_sides), 5)
