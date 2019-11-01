from unittest import TestCase

import sud


class TestCreate_dungeon(TestCase):
    def test_create_dungeon_game_board_has_5_rows(self):
        board = sud.create_dungeon()

        self.assertEqual(len(board), 5)
