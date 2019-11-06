from unittest import TestCase

from A3.sud import validate_move


class TestValidate_move(TestCase):
    def test_validate_move_with_valid_input(self):
        moves = ('n', 's', 'e', 'w')

        for move in moves:
            self.assertTrue(validate_move(move))

    def test_validate_move_with_valid_input_in_caps(self):
        moves = ('N', 'S', 'E', 'W')

        for move in moves:
            self.assertTrue(validate_move(move))

    def test_validate_move_with_invalid_input(self):
        moves = ('North', '1', 'g', 'north')

        for move in moves:
            self.assertFalse(validate_move(move))
