import io
from unittest import TestCase
from unittest.mock import patch

import dungeonsanddragons


class TestPrint_inventory(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_inventory(self, mock_output):
        list_1 = ["1"]
        list_2 = ["a"]

        expected_output = "1a\n"

        dungeonsanddragons.print_inventory(list_1, list_2)

        self.assertEqual(expected_output, mock_output.getvalue())
