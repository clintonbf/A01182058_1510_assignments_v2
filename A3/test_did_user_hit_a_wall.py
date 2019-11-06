from unittest import TestCase

from A3.sud import did_user_hit_a_wall


class TestDid_user_hit_a_wall(TestCase):
    def test_did_user_hit_a_wall_went_north_at_border(self):
        result = did_user_hit_a_wall('n', {'x-coord': 3, 'y-coord': 0})

        self.assertTrue(result)

    def test_did_user_hit_a_wall_went_north_when_not_at_border(self):
        result = did_user_hit_a_wall('n', {'x-coord': 3, 'y-coord': 3})

        self.assertFalse(result)

    def test_did_user_hit_a_wall_went_south_at_border(self):
        result = did_user_hit_a_wall('s', {'x-coord': 3, 'y-coord': 4})

        self.assertTrue(result)

    def test_did_user_hit_a_wall_went_south_when_not_at_border(self):
        result = did_user_hit_a_wall('s', {'x-coord': 3, 'y-coord': 3})

        self.assertFalse(result)

    def test_did_user_hit_a_wall_went_east_at_border(self):
        result = did_user_hit_a_wall('e', {'x-coord': 4, 'y-coord': 0})

        self.assertTrue(result)

    def test_did_user_hit_a_wall_went_east_when_not_at_border(self):
        result = did_user_hit_a_wall('e', {'x-coord': 3, 'y-coord': 3})

        self.assertFalse(result)

    def test_did_user_hit_a_wall_went_west_at_border(self):
        result = did_user_hit_a_wall('w', {'x-coord': 0, 'y-coord': 4})

        self.assertTrue(result)

    def test_did_user_hit_a_wall_went_west_when_not_at_border(self):
        result = did_user_hit_a_wall('s', {'x-coord': 3, 'y-coord': 3})

        self.assertFalse(result)
