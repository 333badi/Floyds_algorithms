import unittest
from sys import maxsize
from copy import deepcopy
import sys
# Import Floyd-Warshall implementations
from iterative.iterative_floyd import iterative_floyd
from recursion.recursive_floyd import recursive_floyd

sys.path.append('../')

class TestFloydWarshall(unittest.TestCase):

    def setUp(self):
        """ Reset the graph before each test. """
        self.NO_PATH = maxsize
        self.test_graph = [
            [0, 3, self.NO_PATH, 7],
            [8, 0, 2, self.NO_PATH],
            [5, self.NO_PATH, 0, 1],
            [2, self.NO_PATH, self.NO_PATH, 0]
        ]
        self.expected_result = [
            [0, 3, 5, 6],
            [5, 0, 2, 3],  #
            [3, 6, 0, 1],
            [2, 5, 7, 0]
        ]

    def test_iterative_floyd(self):
        """ Test Floyd-Warshall using the iterative approach. """
        from iterative.iterative_floyd import GRAPH as GRAPH_ITERATIVE  # Import after resetting

        # Reset GRAPH properly before running the test
        GRAPH_ITERATIVE[:] = deepcopy(self.test_graph)  

        iterative_floyd()  # Run the iterative version
        self.assertEqual(GRAPH_ITERATIVE, self.expected_result)

    def test_recursive_floyd(self):
        """ Test Floyd-Warshall using the recursive approach. """
        from recursion.recursive_floyd import GRAPH as GRAPH_RECURSIVE  # Import after resetting

        # Reset GRAPH properly before running the test
        GRAPH_RECURSIVE[:] = deepcopy(self.test_graph)

        recursive_floyd(0, 0, 0)  # Start recursion
        self.assertEqual(GRAPH_RECURSIVE, self.expected_result)

if __name__ == "__main__":
    unittest.main()