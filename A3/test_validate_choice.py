from unittest import TestCase

from A3.sud import validate_choice


class TestValidate_move(TestCase):
    def test_validate_move_with_valid_input(self):
        choices = ('n', 's', 'e', 'w')
        valid_choices = ('n', 's', 'e', 'w')

        for choice in choices:
            self.assertTrue(validate_choice(choice, valid_choices))

    def test_validate_move_with_valid_input_in_caps(self):
        choices = ('N', 'S', 'E', 'W')
        valid_choices = ('n', 's', 'e', 'w')

        for choice in choices:
            self.assertTrue(validate_choice(choice, valid_choices))

    def test_validate_move_with_invalid_input(self):
        choices = ('North', '1', 'g', 'north')
        valid_choices = ('n', 's', 'e', 'w')

        for choice in choices:
            self.assertFalse(validate_choice(choice, valid_choices))
