from unittest import TestCase
from collections import deque

class VertexConnectivity(TestCase):

    tests = [
        (
            [
                [0, 1, 1, 0],
                [0, 0, 0, 1],
                [0, 1, 0, 0],
                [0, 0, 1, 0]
            ],
            True
        ),
        (
            [
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [0, 1, 0, 0],
                [0, 0, 0, 0]
            ],
            False
        ),
        (
            [
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [1, 0, 0, 0]
            ],
            True
        ),
        (
            [
                [0, 0, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1],
                [1, 0, 0, 0]
            ],
            True
        ),
        (
            [
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            False
        ),
        (
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 1, 0],
                [0, 0, 0, 1]
            ],
            False
        ),
        (
            [
                [0, 1, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]
            ],
            False
        ),
    ]

    @staticmethod
    def func(graph):
        """
        Problem 3
        Runtime: O(V+E) via Kosaraju's Algorithm

        Give an efficient algorithm which takes as input a directed graph G = (V, E), and determines
        whether or not there is a vertex s ∈ V from which all other vertices are reachable.
        """

        def dfs(v, visited, stack):
            visited[v] = True
            for u in range(len(graph)):
                if graph[v][u] and not visited[u]:
                    dfs(u, visited, stack)
            stack.append(v)

        n = len(graph)
        visited = [False] * n
        stack = []

        for v in range(n):
            if not visited[v]:
                dfs(v, visited, stack)

        visited = [False] * n
        scc_count = 0

        while stack:
            v = stack.pop()
            if not visited[v]:
                dfs(v, visited, [])
                scc_count += 1

        return scc_count == 1

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = VertexConnectivity.func(test[0])
            self.assertEqual(output, test[1])
