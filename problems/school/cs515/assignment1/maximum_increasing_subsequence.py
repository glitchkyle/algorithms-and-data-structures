from unittest import TestCase


class MaximumIncreasingSubsequence(TestCase):

    tests = [
        ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11], [8, 12, 14]),
        ([1, 2, 3, 4, 5, 1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
        ([5, 4, 3, 2, 1, 5, 9], [4, 5, 9]),
        ([10, 5, 4, 3, 7, 8, 2, 1, 10, 13, 14, 15], [5, 7, 8, 10, 13, 14, 15]),
        ([2, 4, 6, 8, 10, 2, 4, 6, 8, 10], [2, 4, 6, 8, 10]),
        ([3, 3, 3, 3, 3], [3]),
        ([9, 7, 5, 3, 1, 9, 7, 5, 3, 1], [7, 9]),
        ([12, 3, 7, 8, 10, 12, 3, 7, 8, 10], [3, 7, 8, 10, 12]),
        ([6, 7, 8, 1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7]),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]),
        ([7, 5, 3, 1, 2, 4, 6, 8, 10, 7], [1, 2, 4, 6, 8, 10]),
    ]

    @staticmethod
    def func(seq):
        """
        Problem 2
        Runtime: O(n^2), n = len(seq)

        Maximum Sum Increasing Subsequence Problem: Find a subsequence of a given sequence
        such that the subsequence sum is as high as possible, and the subsequence’s elements are
        sorted in ascending order. This subsequence is not necessarily contiguous or unique. Please
        note that the problem specifically targets subsequences that need not be contiguous, i.e.,
        subsequences are not required to occupy consecutive positions within the original
        sequences.

        For example, consider subsequence {0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11}. The maximum
        sum increasing subsequence is {8, 12, 14} which has sum 34.
        """

        # Implementation assumes that
        # 1. There will always be one number in sequence
        # 2. Sequence contains positive integers

        n = len(seq)
        sums = [num for num in seq]

        for i in range(n):
            for j in range(i):
                if seq[j] < seq[i]:
                    sums[i] = max(sums[i], sums[j] + seq[i])

        # Backtrack from array
        out = []
        current_num = max(sums)
        for i in range(len(seq) - 1, -1, -1):
            if sums[i] == current_num:
                if seq[i] > 0:
                    out.append(seq[i])
                current_num -= seq[i]

        return out[::-1]

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = MaximumIncreasingSubsequence.func(test[0])
            self.assertEqual(output, test[1])
