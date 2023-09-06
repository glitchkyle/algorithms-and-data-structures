from unittest import TestCase

class LongestCommonSubstring(TestCase):

    tests = [
        ("ABABC", "BABCA", "BABC"),
        ("", "BABCA", ""),
        ("XYZ", "123", ""),
        ("OpenAI", "OpenAI is great", "OpenAI"),
        ("", "", ""),
        ("abcdefg", "abcxyz", "abc"),
        ("hello world", "world", "world"),
        ("banana", "cabanaxyz", "bana"),
        ("OpenAI", "openai", "pen"),
        ("ab@c$d", "x@abc$de", "c$d"),
        ("abcdef", "xyzabcdefpqr", "abcdef"),
        ("", "VeryLongStringWithNoCommonSubstring", ""),
        ("a", "a", "a"),
    ]

    @staticmethod
    def func(word1, word2):
        """
        Problem 1
        Runtime: O(m*n), m = len(word1), n = len(word2)

        Longest Common Substring Problem: The longest common substring problem is the
        problem of finding the longest string (or strings) that is a substring (or are substrings) of two
        strings. The problem differs from the problem of finding the Longest Common Subsequence
        (LCS). Unlike subsequences, substrings are required to occupy consecutive positions within
        the original string.

        For example, the longest common substring of strings ABABC, BABCA is the string BABC
        having length 4. Other common substrings are ABC, A, AB, B, BA, BC, and C.
        """
        m = len(word1)
        n = len(word2)

        row_len = m + 1
        column_len = n + 1
        lst = [[0 for _ in range(column_len)] for _ in range(row_len)]

        max_len = 0
        final_idx = 0
        for i in range(1, row_len):
            for j in range(1, column_len):
                if word1[i - 1] == word2[j - 1]:
                    lst[i][j] = 1 + lst[i - 1][j - 1]
                    if lst[i][j] > max_len:
                        max_len = lst[i][j]
                        final_idx = i
                else:
                    lst[i][j] = 0

        return word1[final_idx - max_len : final_idx]

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 3)
            output = LongestCommonSubstring.func(test[0], test[1])
            self.assertEqual(output, test[2])
