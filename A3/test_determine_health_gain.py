from unittest import TestCase

from A3.character import determine_health_gain


class TestDetermine_health_gain(TestCase):
    def test_determine_health_gain_at_max_health(self):
        self.assertEqual(determine_health_gain(5, 5), 0)

    def test_determine_health_gain_at_minus_1_health(self):
        self.assertEqual(determine_health_gain(4, 5), 1)

    def test_determine_health_gain_at_health_deficit_exceeding_2(self):
        self.assertEqual(determine_health_gain(2, 5), 2)
