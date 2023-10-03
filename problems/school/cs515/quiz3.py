from unittest import TestCase

class RobotPath(TestCase):

    tests = [
        (
            [
                [0,0,0],
                [0,1,0],
                [0,0,0]
            ],
            2
        ),
        (
            [
                [0, 1, 0],
                [1, 0, 0],
                [0, 0, 0]
            ],
            0
        ),
        (
            [
                [0, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            6
        ),
        (
            [
                [1, 0, 0],
                [0, 0, 0],
                [0, 0, 0]
            ],
            0
        ),
        (
            [[0]],
            1
        )
    ]

    @staticmethod
    def func(grid):
        """
        Grid-Based Robot Path Count: Given an m x n grid, where a robot is initially located at the top-left corner
        (0, 0) and can only move either down or right at any point in time. The robot's goal is to reach the
        bottom-right corner (m-1, n-1) of the grid. In each cell of the grid, there may be obstacles represented
        by a value of 1, while empty cells are represented by a value of 0. The robot cannot move through cells
        with obstacles.

        Find the total number of unique paths the robot can take to reach the bottom-right corner of the grid,
        considering the obstacle cells as barriers. For simplicity, assume that the robot will always be able to
        move either down or right at any point in time.

        O(m*n), m = len(grid), n = len(grid[0])
        """
        # Check if there is at least a starting point
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        
        # Check if the start is not an obstacle
        if grid[0][0] == 1:
            return 0
        
        m, n = len(grid), len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        # Initialize the first cell as 1 since there is only one way to traverse it
        dp[0][0] = 1 if grid[0][0] == 0 else 0

        # Fill in first column because it is an edge case with no left
        for i in range(1, m):
            # If there is a way to reach the node, it is how many ways to reach the node before
            dp[i][0] = dp[i-1][0] if grid[i][0] == 0 else 0

        # Fill in the first row because it is an edge case with no top
        for j in range(1, n):
            # If there is a way to reach the node, it is how many ways to reach the node before
            dp[0][j] = dp[0][j-1] if grid[0][j] == 0 else 0

        # Check how many ways to can reach a certain grid node
        # dp[i][j] is left + top where
        # left = # of ways to reach dp[i][j-1]
        # top = # of ways to reach dp[i-1][j]
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 0:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        return dp[m-1][n-1]

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = RobotPath.func(test[0])
            self.assertEqual(output, test[1])
