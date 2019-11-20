from unittest import TestCase

from A4.question_3 import dijkstra


class TestDijkstra(TestCase):
    def test_dijkstra_several_items_random_order(self):
        lst = ['white', 'blue', 'blue', 'red', 'white', 'red', 'white']
        expected_end = ['red', 'red', 'white', 'white', 'white', 'blue', 'blue']
        dijkstra(lst)

        self.assertEqual(expected_end, lst)

    def test_dijkstra_items_already_in_order(self):
        lst = ['red', 'white', 'blue']
        expected_end = ['red', 'white', 'blue']
        dijkstra(lst)

        self.assertEqual(expected_end, lst)

    def test_dijkstra_first_item_is_red(self):
        lst = ['red', 'blue', 'white', 'red', 'white']
        expected_end = ['red', 'red', 'white', 'white', 'blue']
        dijkstra(lst)

        self.assertEqual(expected_end, lst)
