from unittest import TestCase

class MinimumSumPartition(TestCase):

    tests = [
        ([10, 20, 15, 5, 25], 5),
        ([1, 2, 3, 4], 0),
        ([3, 1, 4, 2, 2, 1], 1)
    ]

    @staticmethod
    def func(nums):
        """
        Minimum Sum Partition Problem
        
        Given a set of positive integers S, partition set S into two subsets, S1 and S2, such that the difference 
        between the sum of elements in S1 and S2 is minimized. 

        The solution should return the minimum absolute difference between the sum of elements of two partitions.

        Input: S = {10, 20, 15, 5, 25}.
        Output: 5
        """

        nums_length = len(nums)
        summation = sum(nums)

        row_len = nums_length + 1
        column_len = summation + 1
        dp = [[0 for _ in range(column_len)] for _ in range(row_len)]

        for i in range(row_len):
            dp[i][0] = 1

        for i in range(row_len):
            for j in range(1, column_len):
                dp[i][j] = dp[i-1][j]
                # Checking if paired number will be enough to create the current sum j
                if nums[i - 1] <= j:
                    dp[i][j] |= dp[i - 1][j - nums[i - 1]]
        
        # Iterating half of the summation due to communicative property of array
        for j in range(summation // 2, -1, -1):
            # Everything in the last column indicates the possible sum of sets
            if dp[nums_length][j] == True:
                # Summation - 2*S_2 = absolute difference
                return summation - (2 * j)


    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = MinimumSumPartition.func(test[0])
            self.assertEqual(output, test[1])
