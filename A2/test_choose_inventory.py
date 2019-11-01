import io
from unittest import TestCase
from unittest.mock import patch

import dungeonsanddragons


class TestChoose_inventory(TestCase):
    @patch('builtins.input',
           side_effect=[1, -1, 2, -1, 3, -1, 4, -1, 5, -1, 6, -1, 7, -1, 8, -1, 9, -1, 10, -1, 11, -1, 12,
                        -1, 13, -1, 14, -1, 15, -1, 16, -1])
    def test_choose_inventory_item_gets_added(self, mock_choice):
        gear_list = ["Rapier", "Broadsword", "Vorpal sword", "The constrictor", "A duck!", "giant spoon", "icingdeath",
                     "bag of holding", "boomstick", "stabstick", "greaves", "gambeson", "vambraces", "wand of fire",
                     "Twinkle", "Cucumber salad"]

        for gear in gear_list:
            test_gear = dungeonsanddragons.choose_inventory()

            self.assertEqual(test_gear[0], gear)

    @patch('builtins.input', return_value=-1)
    def test_choose_inventory_no_items(self, mock_choice):
        test_gear = dungeonsanddragons.choose_inventory()

        self.assertEqual(len(test_gear), 0)

    @patch('builtins.input', side_effect=[999, -1])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_choose_inventory_invalid_items(self, mock_output, mock_choice):
        test_gear = dungeonsanddragons.choose_inventory()

        expected_output = "Sorry, we don't sell that.\nWhat would you like to purchase?\n"

        self.assertIn(expected_output, mock_output.getvalue())
