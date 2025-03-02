"""
This module has a simple implementation of Floyd's Algorithm
It contains three main functions:
    main -> controls the execution of the script
    print_out_graph -> prints out the graph with nodes and distances
    recursive_floyd -> computes shortest path and updates the GRAPH

The global variables are:
    NO_PATH = Marker for where there is no path. This is the max value of an integer
    GRAPH = Contains the distances for the graph. Node names are inferred by the position
    of the node, i.e. position  0 0 in the list is node 0
    MAX_LENGTH = The size of the graph
    MIN_LEVEL = The lowest search level for the shortest path calculation
    NO_PATH_MARKER = Holder for no path possible. This is used for the printing function. 
"""
from sys import maxsize

NO_PATH = maxsize
GRAPH = [[0,   7,  NO_PATH, 8],
         [NO_PATH,  0,  5,  NO_PATH],
         [NO_PATH, NO_PATH, 0,   2],
         [NO_PATH, NO_PATH, NO_PATH, 0]]

MAX_LENGTH = len(GRAPH[0])
MIN_LEVEL = 0
NO_PATH_MARKER = "No Path"

def main():
    """
    This is the calling function for the recursive Floyd's algorithm
    """
    recursive_floyd(0, 0, 0)  # Start recursion from (0, 0, 0)

    # Uncomment next line when you have completed the task
    print_out_graph()

def print_out_graph():
    """
    This function prints out the graph with the distances
    and a place holder for no path between nodes
    """
    for start_node in range(0, MAX_LENGTH):
        for end_node in range(0, MAX_LENGTH):
            distance = GRAPH[start_node][end_node]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER 

            message = "Distance from Node %s to Node %s is %s" % (start_node, end_node, distance)
            print(message)

def recursive_floyd(outer_loop: int, middle_loop: int, inner_loop: int):
    """
    This function computes the shortest path between each pair of nodes.
    It compares direct paths with paths that have intermediate nodes.

    The function uses recursion instead of a loop to iterate over nodes.

    param: outer_loop: This variable represents the first loop of the iterative version
    param: middle_loop: This variable represents the second loop of the iterative version
    param: inner_loop: This variable represents the last loop of the iterative version
    """
    if outer_loop >= MAX_LENGTH:  # Base case: All intermediate nodes checked
        return

    if middle_loop >= MAX_LENGTH:  # Move to next intermediate node
        recursive_floyd(outer_loop + 1, 0, 0)
        return

    if inner_loop >= MAX_LENGTH:  # Move to next row in the matrix
        recursive_floyd(outer_loop, middle_loop + 1, 0)
        return

    if middle_loop != inner_loop:  # Avoid self-loops
        GRAPH[middle_loop][inner_loop] = min(
            GRAPH[middle_loop][inner_loop],
            GRAPH[middle_loop][outer_loop] + GRAPH[outer_loop][inner_loop]
        )

    # Recur for next inner loop
    recursive_floyd(outer_loop, middle_loop, inner_loop + 1)

if __name__ == "__main__":
    main()
