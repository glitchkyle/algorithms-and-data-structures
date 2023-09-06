from unittest import TestCase


class CountPatterns(TestCase):

    tests = [
        ("subsequence", "sue", 7),
        ("sub", "subsequence", 0),
        ("abacaba", "aba", 6),
        ("subsubsub", "sbs", 4),
        ("abcabcabc", "abc", 10),
        ("test", "", 1),
        ("", "pattern", 0),
        ("aaaaa", "a", 5),
        ("hello, world!", "h,o", 1),
        ("pattern","pattern",1)
    ]

    @staticmethod
    def func(word, pattern):
        """
        Problem 3
        Runtime: O(m*n), m = len(word), n = len(pattern)

        Count the number of times a pattern appears in a given string as a subsequence. Given a
        string, count the number of times a given pattern appears in it as a subsequence. Please
        note that the problem specifically targets subsequences that need not be contiguous, i.e.,
        subsequences are not required to occupy consecutive positions within the original
        sequences.

        For example, Input: string = “subsequence” pattern = “sue”
        """
        word_len = len(word)
        pattern_len = len(pattern)

        row_len = pattern_len + 1
        column_len = word_len + 1
        dp = [[0 for _ in range(column_len)] for _ in range(row_len)]

        for i in range(column_len):
            dp[0][i] = 1

        for i in range(1, row_len):
            for j in range(1, column_len):
                if word[j - 1] == pattern[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
                else:
                    dp[i][j] = dp[i][j - 1]

        return dp[pattern_len][word_len]

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 3)
            output = CountPatterns.func(test[0], test[1])
            self.assertEqual(output, test[2])
