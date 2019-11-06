from unittest import TestCase

from A3.sud import move_char


class TestMove_char(TestCase):
    def test_move_char_move_north(self):
        c = {'x-coord': 3, 'y-coord': 3}
        move_char('n', c)

        self.assertEqual(c['y-coord'], 2)

    def test_move_char_move_south(self):
        c = {'x-coord': 3, 'y-coord': 3}
        move_char('s', c)

        self.assertEqual(c['y-coord'], 4)

    def test_move_char_move_east(self):
        c = {'x-coord': 3, 'y-coord': 3}
        move_char('e', c)

        self.assertEqual(c['x-coord'], 4)

    def test_move_char_move_west(self):
        c = {'x-coord': 3, 'y-coord': 3}
        move_char('w', c)

        self.assertEqual(c['x-coord'], 2)

