from unittest import TestCase


class Ancestry(TestCase):

    tests = [
        (
            [
                [0, 0, 0, 1, 0, 0, 0, 0],
                [1, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 1],
                [0, 0, 0, 0, 0, 0, 1, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ], 
            1, 
            ([2, 1, 12, 3, 4, 13, 5, 8], [11, 16, 15, 10, 7, 14, 6, 9])
        )
    ]

    @staticmethod
    def func(graph, root):
        """
        Problem 2

        Node A is an ancestor of a node B if and only if 
        pre_visit_list[A] < pre_visit_list[B] and post_visit_list[A] > post_visit_list[B]
        Preprocessing: O(V+E) because of tree structure
        Lookup Runtime: O(1)

        You are given a binary tree T = (V, E) (in adjacency list format), along with a designated root
        node r ∈ V. Recall that u is said to be an ancestor of v in the rooted tree, if the path from r
        to v in T passes through u. You wish to preprocess the tree so that queries of the form “is u
        an ancestor of v?” can be answered in constant time. The preprocessing itself should take
        linear time. How can this be done?
        """

        # Assumptions
        # 1. Root is a 0 <= number < len(graph)

        n = len(graph)

        clock = 1
        visited = [False for _ in range(n)]
        pre_visit_list = [0 for _ in range(n)]
        post_visit_list = [0 for _ in range(n)]

        stack = [root]
        while stack:
            node = stack[-1]
            if not visited[node]:
                visited[node] = True
                pre_visit_list[node] = clock
                clock += 1
            
            unvisited_neighbors = [i for i, val in enumerate(graph[node]) if val == 1 and not visited[i]]

            if unvisited_neighbors:
                stack.append(unvisited_neighbors[0])
            else:
                post_visit_list[node] = clock
                clock += 1
                stack.pop()

        return pre_visit_list, post_visit_list

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 3)
            output = Ancestry.func(test[0], test[1])
            self.assertEqual(output, test[2])
