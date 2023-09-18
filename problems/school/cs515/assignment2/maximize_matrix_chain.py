from unittest import TestCase

class MaximizeMatrixChain(TestCase):

    tests = [
        ([2, 3, 4, 5], 90),
        ([5, 4, 3, 2], 90),
        ([1, 1, 1, 1], 2),
        ([10, 20, 30, 40], 32000),
        ([2, 2, 2, 2], 16),
        ([3, 4, 2, 1], 30),
        ([4, 3, 2, 1], 32),
        ([1, 2, 3, 4], 32),
        ([2, 1, 4, 3], 32),
        ([3, 3, 1, 2], 24),
        ([7, 8, 6, 5, 4, 3], 770)
    ]

    @staticmethod
    def func(dimensions):
        """
        Problem 4
        O(n^3), n = len(dimensions)

        Consider a variant of the matrix-chain multiplication problem in which the goal is to
        parenthesize the sequence of matrices to maximize, rather than minimize.
        """
        size = len(dimensions)
        dp = [[0 for _ in range(size)] for _ in range(size)]

        for length in range(2, size):
            for i in range(1, len(dimensions) - 1 - length + 2):
                j = i + length - 1
                for k in range(i, j):
                    calculation = dimensions[i-1] * dimensions[k] * dimensions[j]
                    q = dp[i][k] + dp[k+1][j] + calculation
                    dp[i][j] = max(q, dp[i][j])
        
        return dp[1][len(dimensions) - 1]

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = MaximizeMatrixChain.func(test[0])
            self.assertEqual(output, test[1])
