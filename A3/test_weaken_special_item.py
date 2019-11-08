import io
from unittest import TestCase
from unittest.mock import patch

from A3.sud import weaken_special_item


class TestWeaken_special_item(TestCase):
    def test_weaken_special_item_weakens(self):
        p = {'doctor-note': {'existence': True, 'durability': 4}}

        weaken_special_item(p)

        self.assertEqual(p['doctor-note']['durability'], 3)

    def test_weaken_special_item_destruction_occurs(self):
        p = {'doctor-note': {'existence': True, 'durability': 1}}

        weaken_special_item(p)

        self.assertFalse(p['doctor-note']['existence'])

    def test_weaken_special_item_destruction_occurs_sets_durability_to_0(self):
        p = {'doctor-note': {'existence': True, 'durability': 1}}
        weaken_special_item(p)

        self.assertEqual(p['doctor-note']['durability'], 0)

    def test_weaken_special_item_destruction_occurs_sets_dex_to_10(self):
        p = {'Dexterity': 99, 'doctor-note': {'existence': True, 'durability': 1}}
        weaken_special_item(p)

        self.assertEqual(p['Dexterity'], 10)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_weaken_special_item_destruction_occurs_prints_msg(self, mock_output):
        p = {'doctor-note': {'existence': True, 'durability': 1}}
        weaken_special_item(p)

        self.assertEqual(mock_output.getvalue(), "Your doctor's note has disintegrated! "
                                                 "Ah well: back to good old hard work\n")
