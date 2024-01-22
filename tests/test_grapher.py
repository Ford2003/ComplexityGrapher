import unittest
from src.grapher import *


class TestGrapher(unittest.TestCase):
    def test_non_callable(self):
        self.assertRaises(TypeError, graph_time, '', [])

    def test_callable(self):
        def foo():
            pass
        graph_time(foo, [])

    def test_empty_params(self):
        graph_time(lambda: None, [])

    def test_mismatched_params(self):
        self.assertRaises(TypeError, graph_time, lambda x: x, [[1, 2]])
        self.assertRaises(TypeError, graph_time, lambda x: ''.join(x), [[1]])

    def test_non_list_param(self):
        self.assertRaises(TypeError, graph_time, lambda: None, 'invalid')

    def test_invalid_plot_type(self):
        self.assertRaises(ValueError, graph_time, sum, [], 'scater')

    def test_valid_plot_type(self):
        graph_time(lambda: None, [], 'scatter')
        graph_time(lambda: None, [], 'line')


if __name__ == '__main__':
    unittest.main()
