from unittest import TestCase

INF = float('inf')

def heapifyMin(graph, arr, size, i):

    # Index position of arrrays as a tree
    smallest = i                # Root
    left = 2 * i + 1            # Left Child
    right = 2 * i + 2           # Right Child

    x1, y1 = arr[smallest]
    smallest_cost = graph[x1][y1]
    
    # Check if left child exists
    if left < size:
        x2, y2 = arr[left]
        left_cost = graph[x2][y2]
        # If left child is smaller than root
        if left_cost < smallest_cost:
            smallest = left
            smallest_cost = left_cost

    # Check if right child exists
    if right < size:
        x3, y3 = arr[right]
        right_cost = graph[x3][y3]
        # If right child is smaller than root
        if right_cost < smallest_cost:
            smallest = right
            smallest_cost = right_cost

    # If smallest is not the current root, switch current root to smallest
    if smallest != i:
        arr[smallest], arr[i] = arr[i], arr[smallest]
        heapifyMin(graph, arr, size, smallest)

def heapifySort(graph, arr):
    startIndex = len(arr) // 2 - 1
    for i in range(startIndex, -1, -1):
        heapifyMin(graph, arr, len(arr), i)

class MinimumCostPath(TestCase):

    tests = [
        (
            [
                [4, 7, 8, 6, 4],
                [6, 7, 3, 9, 2], 
                [3, 8, 1, 2, 4], 
                [7, 1, 7, 3, 7], 
                [2, 9, 8, 9, 3], 
            ],
            36
        ),
        (
            [
                [3,  2,  4],
                [1,  8,  2],
                [6,  3,  5],
                [7,  4,  2]
            ],
            18
        ),
        (
            [
                [1, 3, 4],
                [1, 5, 1],
                [4, 2, 1]
            ],
            9
        ),
        (
            [
                [1, 3, 1],
                [1, 5, 1],
                [4, 2, 1]
            ],
            7
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]
            ],
            21
        ),
        (
            [
                [5, 2, 7],
                [3, 4, 1],
                [6, 8, 2]
            ],
            14
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6]
            ],
            12
        ),
        (
            [
            [1]
            ],
            1
        ),
        (
            [
                [3, 1],
                [2, 3],
                [4, 2],
                [5, 1]
            ],
            10
        )
    ]

    @staticmethod
    def func(graph):
        """
        Given an M × N matrix of integers where each cell has a cost associated with it, find the
        minimum cost to reach the last cell (M-1, N-1) of the matrix from its first cell (0, 0). We can
        only move one unit right or one unit down from any cell, i.e., from cell (i, j), we can move
        to (i, j+1) or (i+1, j).

        Dijkstra's Algorithm: O(v^2) but O((v+e)log(v)) if priority queue is implemented
        """

        m, n = len(graph), len(graph[0])
        dist = [[INF for _ in range(n)] for _ in range(m)]
        dist[0][0] = graph[0][0]

        open_list = []
        closed_list = []

        open_list.append((0, 0))

        while len(open_list) > 0:

            current_search_node = open_list.pop(0)
            closed_list.append(current_search_node)
            x, y = current_search_node

            # Path found
            if x == m - 1 and y == n - 1:
                break
            
            # Get neighbors
            neighbors = []

            # Down
            if x + 1 <= m-1:
                neighbors.append((x + 1, y))

            # Right
            if y + 1 <= n-1:
                neighbors.append((x, y + 1))

            # Searching traversable nodes and assigning costs
            current_search_node_cost = dist[x][y]
            for neighbor in neighbors:

                # Do not search if it has already been searched
                if neighbor in closed_list:
                    continue

                neighbor_x, neighbor_y = neighbor

                cost_to_neighbor = graph[neighbor_x][neighbor_y]
                total_cost = current_search_node_cost + cost_to_neighbor

                dist[neighbor_x][neighbor_y] = min(
                    dist[neighbor_x][neighbor_y],
                    total_cost
                )

                open_list.append(neighbor)

                # Sort so that minimum is at the top of tree
                heapifySort(graph, open_list)

        return dist[m-1][n-1]

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = MinimumCostPath.func(test[0])
            self.assertEqual(output, test[1])
