from unittest import TestCase

from A4.question_8 import im_not_sleepy


class TestIm_not_sleepy(TestCase):
    def test_im_not_sleepy_generates_10_08(self):
        expected_output = "The time with the highest bars is 10:08 The number of bars is 21"
        self.assertEqual(expected_output, im_not_sleepy())
