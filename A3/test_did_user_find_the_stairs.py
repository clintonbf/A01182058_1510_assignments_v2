import io
from unittest import TestCase
from unittest.mock import patch

from A3.sud import did_user_find_the_stairs


class TestDid_user_find_the_stairs(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_did_user_find_the_stairs_stairs_were_found_and_msg_printed(self, mock_output):
        did_user_find_the_stairs(1, {'Floor': 3})

        self.assertIn("Success! You made it to the stairs down!\n", mock_output.getvalue())

    def test_did_user_find_the_stairs_stairs_were_found_and_floor_decremented(self):
        p = {'Floor': 3}
        did_user_find_the_stairs(1, p)

        self.assertEqual(p['Floor'], 2)