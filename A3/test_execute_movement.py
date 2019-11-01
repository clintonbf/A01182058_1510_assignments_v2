from unittest import TestCase

import sud


class TestExecute_movement(TestCase):
    def test_execute_movement_north_with_space(self):
        new_loc = sud.execute_movement([1, 2], 1)

        self.assertEqual(new_loc[1], 3)

    def test_execute_movement_south_with_space(self):
        new_loc = sud.execute_movement([1, 2], 2)

        self.assertEqual(new_loc[1], 1)

    def test_execute_movement_east_with_space(self):
        new_loc = sud.execute_movement([2, 1], 3)

        self.assertEqual(new_loc[0], 3)

    def test_execute_movement_west_with_space(self):
        new_loc = sud.execute_movement([2, 1], 4)

        self.assertEqual(new_loc[0], 1)

    def test_execute_movement_north_without_space(self):
        new_loc = sud.execute_movement([1, 5], 1)

        self.assertEqual(new_loc[1], 5)

    def test_execute_movement_south_without_space(self):
        new_loc = sud.execute_movement([1, 0], 2)

        self.assertEqual(new_loc[1], 0)

    def test_execute_movement_east_without_space(self):
        new_loc = sud.execute_movement([5, 1], 3)

        self.assertEqual(new_loc[0], 5)

    def test_execute_movement_west_without_space(self):
        new_loc = sud.execute_movement([0, 1], 4)

        self.assertEqual(new_loc[0], 0)
