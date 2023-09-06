from unittest import TestCase

class DiffUtility(TestCase):
    
    tests = [("XMJYAUZ", "XMJAATZ", "X M J -Y A -U +A +T Z")]

    @staticmethod
    def func(X, Y):
        """
        Problem 4
        Runtime: O(m*n), m = len(X), n = len(Y)

        Implement Diff Utility: Implement your diff utility, i.e., given two similar strings, efficiently
        list out all differences between them. The diff utility is a data comparison tool that
        calculates and displays the differences between the two texts. It tries to determine the
        smallest set of deletions and insertions and create one text from the other. Diff is line-
        oriented rather than character-oriented, unlike edit distance.
        For example, Input: string X = XMJYAUZ string Y = XMJAATZ

        Output:
        X M J -Y A -U +A +T Z
        (- indicates that character is deleted from Y but it was present in X)
        (+ indicates that character is inserted in Y but it was not present in X)
        """

        # Create a matrix data structure similar to edit distance problem

        m = len(X)
        n = len(Y)
        out = [[0 for _ in range(m+1)] for _ in range(n+1)]
        
        for i in range(1, n+1):
            for j in range(1,m+1):
                if Y[i - 1] == X[j - 1]:
                    out[i][j] = out[i-1][j-1] + 1
                else:
                    out[i][j] = max(out[i-1][j], out[i][j-1])

        # Backtrack from 2D path

        i, j = n, m
        out_str = []

        while i > 0 and j > 0:
            if X[j - 1] == Y[i - 1]:
                out_str.append(X[j - 1])
                j -= 1
                i -= 1
            elif out[i-1][j] == out[i][j]:
                out_str.append(f"+{Y[i-1]}")
                i -= 1
            else:
                out_str.append(f"-{X[j-1]}")
                j -= 1

        # Cleanup
        
        while i > 0:
            out_str.append(f"+{Y[i-1]}")
            i -= 1

        while j > 0:
            out_str.append(f"-{X[j-1]}")
            j -= 1

        return ' '.join(out_str[::-1])
    
    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 3)
            output = DiffUtility.func(test[0], test[1])
            self.assertEqual(output, test[2])