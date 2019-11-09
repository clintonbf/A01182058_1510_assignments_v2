import io
from unittest import TestCase
from unittest.mock import patch

from A3.sud import apply_god_modification


class TestApply_god_modification(TestCase):
    def test_apply_god_modification_no_god(self):
        options = ['stairs', 'item']

        for option in options:
            self.assertEqual(apply_god_modification(option, False), 0)

    def test_apply_god_modification_god_and_item_or_stairs(self):
        options = ['stairs', 'item']
        expected_output = [9, 14]

        for i in range(len(options)):
            self.assertEqual(apply_god_modification(options[i], True), expected_output[i])
