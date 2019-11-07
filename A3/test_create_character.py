from unittest import TestCase

from A3 import character


class TestCreate_character(TestCase):
    def test_create_character_attributes(self):
        c = character.create_character()

        expected_attr = {'Name': 'Anonymous', 'Dexterity': 10, 'Class': 'student', 'HP': {'Current': 10, 'Max': 10},
                         'Attacks': ['studiousness', 'hard work', 'collaboration', 'academic integrity'],
                         'x-coord': 0, 'y-coord': 0}

        for k in c:
            self.assertEqual(c[k], expected_attr[k])
