from unittest import TestCase

INF = float('inf')

class ModifiedBellmanFord(TestCase):

    tests = [
        (
            [
                [0, 5, INF, INF, INF, INF],
                [INF, 0, 1, 2, INF, INF], 
                [INF, INF, 0, INF, 1, INF], 
                [INF, INF, INF, 0, INF, 2], 
                [INF, INF, INF, -1, 0, INF], 
                [INF, INF, INF, INF, -3, 0]
            ],
            0, [0, 5, 6, 2, 2, 5]
        ),
        (
            [
                [0, 1, INF],
                [INF, 0, -1],
                [-1, INF, 0]
            ], 
            0, [-2, 0, -1]
        ),
        (
            [
                [0, INF, INF],
                [INF, 0, INF],
                [INF, INF, 0]
            ],
            0, [0, INF, INF]
        ),
        (
            [
                [0]
            ],
            0, [0]
        )
    ]

    @staticmethod
    def func(graph, source):
        """
        Modify the Bellman-Ford algorithm to return the shortest path from a given start vertex S in
        a directed graph G. If there is a negative weight cycle, reachable from S, output the vertices.

        O(v^3), v = len(graph)
        """

        # Assumption
        # Problem: Given a start vertex S, find all paths to other vertices
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

        v = len(graph)

        # Creating new array to prevent shallow copy and modify weights of graph
        # New array will be all shortest path from source
        paths = [num for num in graph[source]]

        # Only need to do v - 1 iterations for relaxation
        for _ in range(v - 1):
            # Iterate through every edge of every vertex
            for i in range(v):
                for j in range(v):
                    if graph[i][j] != INF:
                        # Path exists and there could be a shorter path
                        paths[j] = min(paths[j], paths[i] + graph[i][j])

        output = [num for num in paths]
        
        # Check for negative weight cycles by completing one more iteration
        for i in range(v):
            for j in range(v):
                if graph[i][j] != INF:
                    if paths[j] > paths[i] + graph[i][j]:
                        print(f"\nNegative weight cycle to vertex {i + 1}")
                        paths[j] = paths[i] + graph[i][j]

        return output

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 3)
            output = ModifiedBellmanFord.func(test[0], test[1])
            self.assertEqual(output, test[2])
