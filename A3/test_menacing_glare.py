import io
from unittest import TestCase
from unittest.mock import patch

from A3.sud import menacing_glare


class TestMenacing_glare(TestCase):
    @patch('random.choice', side_effect=['Chris'])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_menacing_glare_chris_wanders_by(self, mock_output, mock_choice):
        menacing_glare()

        expected_output = "Chris wanders by the the newly vacated exit, holding final exam; peering right at you...\n"

        self.assertEqual(mock_output.getvalue(), expected_output)
