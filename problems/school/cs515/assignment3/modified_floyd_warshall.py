from unittest import TestCase

INF = float('inf')

class ModifiedFloydWarshall(TestCase):

    tests = [
        (
            [
                [0, INF, -2, INF],
                [4, 0, 3, INF], 
                [INF, INF, 0, 2], 
                [INF, -1, INF, 0],
            ], 
            [
                [0, -1, -2, 0],
                [4, 0, 2, 4], 
                [5, 1, 0, 2], 
                [3, -1, 1, 0], 
            ]
        ),
        (
            [
                [0, 5, INF, INF, INF, INF],
                [INF, 0, 1, 2, INF, INF], 
                [INF, INF, 0, INF, 1, INF], 
                [INF, INF, INF, 0, INF, 2], 
                [INF, INF, INF, -1, 0, INF], 
                [INF, INF, INF, INF, -3, 0]
            ],
            [
                [0, 5, 6, 4, 5, 6],
                [INF, 0, 1, -1, 0, 1], 
                [INF, INF, 0, -2, -1, 0], 
                [INF, INF, INF, -2, -1, 0], 
                [INF, INF, INF, -3, -2, -1], 
                [INF, INF, INF, -6, -5, -4]
            ]
        ),
        (
            [
                [0, 1, INF],
                [INF, 0, -1],
                [-1, INF, 0]
            ],
            [
                [-1, 0, -1],
                [-2, -1, -2],
                [-2, -1, -2]
            ]
        ),
        (
            [
                [0, 3, INF, 5],
                [2, 0, INF, 4],
                [INF, 1, 0, INF],
                [INF, INF, 2, 0]
            ],
            [
                [0, 3, 7, 5],
                [2, 0, 6, 4],
                [3, 1, 0, 5],
                [5, 3, 2, 0]
            ]
        ),
        (
            [
                [0, 5, INF, 6, INF],
                [INF, 0, 1, INF, 7],
                [3, INF, 0, 4, INF],
                [INF, INF, 2, 0, 3],
                [2, INF, INF, 5, 0]
            ],
            [
                [0, 5, 6, 6, 9],
                [4, 0, 1, 5, 7],
                [3, 8, 0, 4, 7],
                [5, 10, 2, 0, 3],
                [2, 7, 7, 5, 0]
            ]
        )
    ]

    @staticmethod
    def func(graph):
        """
        Modify the Floyd-Warshall algorithm to return all-pairs shortest path in a directed graph G.
        If there is a negative weight cycle, output the vertices.

        O(v^3), v = len(graph)
        """

        # Assumption
        # 1. Parameter `graph` is a 2D matrix where the graph[i][j] is the cost from i to j
        # 2. graph is a 2D square with size v x v
        # 3. Source is an integer n where 0 <= n <= len(graph) - 1, making graph[n][n] the source
        # 4. If graph[i][j] is INF, it means that there is no path from i to j
        # 5. Output means print out
        # 6. Negative weight cycle means vertex is part of the cycle

        if len(graph) == 0:
            raise ValueError("Graph must have one valid edge")

        if len(graph) != len(graph[0]):
            raise ValueError("Graph must be a square")
        
        # Make deep copy of graph to prevent modifying parameter
        dist = [row[:] for row in graph]
        v = len(graph)

        for k in range(v):
            for i in range(v):
                for j in range(v):
                    # Take the minimum of either the current path or use an intermediary vertex
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        
        for i in range(v):
            if dist[i][i] < 0:
                print(f"\nNegative weight cycle to vertex {i + 1}")
        
        return dist

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = ModifiedFloydWarshall.func(test[0])
            self.assertEqual(output, test[1])
