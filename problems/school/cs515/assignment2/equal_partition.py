from unittest import TestCase

class EqualPartition(TestCase):

    tests = [
        ([1, 2, 3, 4], True),
        ([4, 2, 1, 3], True),
        ([2, 3, 4, 6], False),
        ([1, 2, 3], True),
        ([4], False),
        ([5, 5, 10, 10], True),
        ([2, 4, 8], False),
        ([1, 2, 2, 3], True),
        ([3, 7, 5, 1, 2, 9], False),
        ([8, 5, 3, 2], False),
        ([10, 12, 15, 17], True)
    ]

    @staticmethod
    def func(sequence):
        """
        Problem 3
        O(n*b), n = len(sequence), b = sum(sequence)

        Equal Subset Sum Partition Problem: you are given a set of positive numbers, find if we can
        partition it into two subsets such that the sum of elements in both the subsets is equal.

        Input: {1, 2, 3, 4} # Sum = 10
        Output: True
        Equal sum: {1, 4} and {2, 3}

        Input: {2, 3, 4, 6} # Sum = 15
        Output: False
        The given set cannot be partitioned into two subsets with an equal sum.
        """

        # Assumptions
        # 1. No duplicate numbers

        # Sequence must have an even sum
        # Where half the sum is the subset sum
        sequence_sum = sum(sequence)
        sequence_len = len(sequence)
        if sequence_sum % 2 != 0 or sequence_len < 2:
            return False
        half_sum = sequence_sum // 2
        
        dp = [0 for _ in range(half_sum + 1)]

        for i in range(sequence_len):
            current_num = sequence[i]
            for j in range(half_sum, current_num - 1, -1):
                if dp[j - current_num] == 1 or j == current_num:
                    dp[j] = 1

        return dp[half_sum]

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = EqualPartition.func(test[0])
            self.assertEqual(output, test[1])
