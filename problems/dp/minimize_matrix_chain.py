from unittest import TestCase

class MinimizeMatrixChain(TestCase):

    tests = [
        ([4, 2, 3, 1, 3], 26),
        ([40, 20, 30, 10, 30], 26000),
        ([1, 2, 3, 4, 3], 30),
        ([10, 20, 30], 6000)
    ]

    @staticmethod
    def func(dimensions):
        size = len(dimensions)
        dp = [[float("inf") for _ in range(size)] for _ in range(size)]

        for i in range(size):
            dp[i][i] = 0

        for length in range(2, size):
            for i in range(1, len(dimensions) - 1 - length + 2):
                j = i + length - 1
                for k in range(i, j):
                    calculation = dimensions[i-1] * dimensions[k] * dimensions[j]
                    q = dp[i][k] + dp[k+1][j] + calculation
                    dp[i][j] = min(q, dp[i][j])
        
        return dp[1][len(dimensions) - 1]

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = MinimizeMatrixChain.func(test[0])
            self.assertEqual(output, test[1])
