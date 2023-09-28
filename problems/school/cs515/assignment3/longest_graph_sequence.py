from unittest import TestCase

class LongestGraphSequence(TestCase):

    tests = [
        (
            [
                [10, 13, 14, 21, 23],
                [11, 9, 22, 2, 3], 
                [12, 8, 1, 5, 4], 
                [15, 24, 7, 6, 20], 
                [16, 17, 18, 19, 25], 
            ],
            [2, 3, 4, 5, 6, 7],
        ),
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [1, 2, 3]
        ),
        (
            [
                [1, 2, 3],
                [6, 5, 4],
                [7, 8, 9]
            ],
            [1, 2, 3, 4, 5, 6, 7, 8, 9]
        ),
        (
            [
                [1, 2, 3, 4, 5],
                [10, 11, 12, 13, 14],
                [9,  8,  7,  6, 15],
                [20, 19, 18, 17, 16],
                [21, 22, 23, 24, 25]
            ],
            [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25]
        )
    ]
    
    @staticmethod
    def func(graph):
        """
        Given an N × N matrix where each cell has a distinct value in the 1 to N × N. Find the longest
        sequence formed by adjacent numbers in the matrix such that for each number, the
        number on the adjacent neighbor is +1 in its value. If we are at location (x, y) in the matrix,
        we can move to (x, y+1), (x, y-1), (x+1, y), or (x-1, y) if the value at the destination cell is one
        more than the value at source cell.

        O(v^2), v = len(graph)
        """

        if len(graph) == 0:
            raise ValueError("Graph must have one valid edge")

        if len(graph) != len(graph[0]):
            raise ValueError("Graph must be a square")

        v = len(graph)

        maximum_sequence = []
        for i in range(v):
            for j in range(v):
                
                # Check if I am not the start of the sequence
                decrement = graph[i][j] - 1
                # Try Left
                if j-1 >= 0 and decrement == graph[i][j-1]:
                    continue
                # Try Right
                elif j+1 < v and decrement == graph[i][j+1]:
                    continue
                # Try Up
                elif i-1 >= 0 and decrement == graph[i-1][j]:
                    continue
                # Try
                elif i+1 < v and decrement == graph[i+1][j]:
                    continue
                
                # Perform depth first search to build sequence
                sequence, stack = [graph[i][j]], [(i, j)]
                while len(stack) > 0:
                    x, y = stack.pop()
                    increment = graph[x][y] + 1

                    # Try Left
                    if y - 1 >= 0 and increment == graph[x][y-1]:
                        sequence.append(graph[x][y-1])
                        stack.append((x, y-1))

                    # Try Right
                    if y + 1 < v and increment == graph[x][y+1]:
                        sequence.append(graph[x][y+1])
                        stack.append((x, y+1))

                    # Try Up
                    if x - 1 >= 0 and increment == graph[x-1][y]:
                        sequence.append(graph[x-1][y])
                        stack.append((x-1, y))

                    # Try Down
                    if x + 1 < v and increment == graph[x+1][y]:
                        sequence.append(graph[x+1][y])
                        stack.append((x+1, y))
                
                if len(sequence) > len(maximum_sequence):
                    maximum_sequence = sequence

        return maximum_sequence

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = LongestGraphSequence.func(test[0])
            self.assertEqual(output, test[1])
