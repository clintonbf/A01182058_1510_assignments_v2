from unittest import TestCase
from unittest.mock import patch

from dungeonsanddragons import zounds


class TestZounds(TestCase):
    @patch('random.choice', side_effect=['Zounds! ', 'Wow! ', 'A crashing blow! ', 'A vicious attack! ',
                                         'A brilliant strike! ', "I'm glad I'm not them! ", "Ka-blamm-o!!! "])
    def test_zounds_a_hit(self, mock_item):
        test_list = ['Zounds! ', 'Wow! ', 'A crashing blow! ', 'A vicious attack! ', 'A brilliant strike! ',
                     "I'm glad I'm not them! ", "Ka-blamm-o!!! "]

        for item in test_list:
            mock_item = zounds(1)
            self.assertEqual(item + "1 damage done!", mock_item)

    @patch('random.choice', side_effect=["A miss!", "Airball!", "Whooooosh!", "A brilliant defence!", "Parried!",
                                         "Were you even aiming at them?", "Defended!", "Nope."])
    def test_zounds_a_miss(self, mock_item):
        test_list = ["A miss!", "Airball!", "Whooooosh!", "A brilliant defence!", "Parried!",
                     "Were you even aiming at them?", "Defended!", "Nope."]

        for item in test_list:
            mock_item = zounds(0)
            self.assertEqual(item, mock_item)
