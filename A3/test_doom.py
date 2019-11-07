from unittest import TestCase
from unittest.mock import patch

from A3.sud import doom


class TestDoom(TestCase):
    @patch('random.choice', side_effect=["The life is leaving Clint", "Light the fires of Ka-bloom! Clint is coming!",
                                         "OOOOOOOH Clint", "Yikes! Look at the bones!!!!",
                                         "The deities will guide Clint to their rest", " Clint: You dead."])
    def test_doom(self, mock_item):
        test_list = ["The life is leaving Clint", "Light the fires of Ka-bloom! Clint is coming!",
                     "OOOOOOOH Clint", "Yikes! Look at the bones!!!!",
                     "The deities will guide Clint to their rest", " Clint: You dead."]

        for item in test_list:
            mock_item = doom("Clint")
            self.assertEqual(item, mock_item)
