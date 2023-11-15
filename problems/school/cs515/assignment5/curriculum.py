from unittest import TestCase

class Curriculum(TestCase):

    tests = [
        (
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [1, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0, 1],
                [0, 0, 1, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1, 0, 0, 0],
            ],
            3
        ),
        (
            [
                [0, 1, 0, 0, 0],
                [0, 0, 1, 0, 0],
                [0, 0, 0, 1, 0],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]
            ],
            5
        ),
        (
            [
                [0, 1, 1, 0, 0, 0],
                [0, 0, 0, 1, 0, 0],
                [0, 0, 0, 1, 1, 0],
                [0, 0, 0, 0, 1, 1],
                [0, 0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0, 0]
            ],
            5
        ),
        (
            [
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ],
            1
        ),
        (
            [
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 1],
                [0, 0, 0, 0, 0]
            ],
            2
        ),
        (
            [
                [0, 1, 1, 1, 1],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0]
            ],
            2
        )
    ]

    @staticmethod
    def func(graph):
        """
        Problem 1
        Runtime: O(V+E)

        Suppose a CS curriculum consists of n courses, all of them mandatory. The prerequisite
        graph G has a node for each course, and an edge from course v to course w if and only if v is
        a prerequisite for w. Find an algorithm that works directly with this graph representation
        and computes the minimum number of semesters necessary to complete the curriculum
        (assume that a student can take any number of courses in one semester). The running time
        of your algorithm should be linear.
        """

        # Assumptions
        # 1. graph[i][j] is an adjacency matrix of either 1 or 0 where 1 means i is a prereq for j (graph[i][j] != graph[j][i])

        def convert_matrix_to_graph(matrix):
            graph = {}
            for i in range(len(matrix)):
                neighbors = {}
                for j in range(len(matrix[0])):
                    if i == j and matrix[i][j] == 1:
                        raise ValueError("Course cannot depend on itself")
                    if matrix[i][j] != 0:
                        neighbors[j] = matrix[i][j]
                graph[i] = neighbors
            return graph

        graph = convert_matrix_to_graph(graph)

        n = len(graph)
        visited = [False] * n
        stack = []

        def topological_sort_util(graph, visited, stack, node):
            visited[node] = True
            for neighbor in graph.get(node, {}):
                if not visited[neighbor]:
                    topological_sort_util(graph, visited, stack, neighbor)
            stack.append(node)

        for i in range(n):
            if not visited[i]:
                topological_sort_util(graph, visited, stack, i)

        dist = [float('-inf')] * n
        dist[stack[-1]] = 0

        while stack:
            node = stack.pop()
            for neighbor, weight in graph.get(node, {}).items():
                dist[neighbor] = max(dist[neighbor], dist[node] + weight)

        return max(dist) + 1


    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = Curriculum.func(test[0])
            self.assertEqual(output, test[1])
