import io
from unittest import TestCase
from unittest.mock import patch

from A3.sud import add_formatting_line


class TestAdd_formatting_line(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_add_formatting_line(self, mock_output):
        add_formatting_line()

        self.assertEqual(mock_output.getvalue(), "~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
