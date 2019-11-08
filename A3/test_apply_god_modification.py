import io
from unittest import TestCase
from unittest.mock import patch


class TestApply_god_modification(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_apply_god_modification(self, mock_output):
        stats = {'items': False, 'stairs': False, 'escape': (1, 2)}

        expected_output = "The exit is at: (1, 2)\n"
        apply_god_modification

        self.assertEqual(expected_output.getvalue(), expected_output)
