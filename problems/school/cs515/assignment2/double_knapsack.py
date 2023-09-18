from unittest import TestCase

class DoubleKnapsack(TestCase):

    tests = [
        ([8, 3, 2], [8, 3, 2], [10, 3], 13),
        ([5, 7, 4], [5, 7, 4], [6, 3], 5),
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], [5, 10], 15),
        ([10, 20, 30], [10, 20, 30], [5, 10], 10),
        ([2, 2, 3, 4, 5], [2, 2, 3, 4, 5], [7, 6], 13),
        ([5, 10, 15], [5, 10, 15], [10, 5], 15),
        ([6, 8, 10, 13, 16], [6, 8, 10, 13, 16], [5, 15], 14),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [5, 5], 5),
        ([3, 6, 9, 12], [3, 6, 9, 12], [6, 12], 18),
        ([10, 15, 5], [10, 15, 5], [5, 10], 15)
    ]

    @staticmethod
    def func(profits, weights, capacities):
        """
        Problem 1
        O(i*j*k), i = len(pj), j = c1, k = c2

        Double Knapsack Problem: Given a set of n items and 2 knapsacks, with

        pj: profit of item j
        wj: weight of item j
        c1: capacity of the first knapsack
        c2: capacity of the second knapsack

        select m disjoint subsets of items so that the total profit of the selected items is a
        maximum, and each subset can be assigned to a different bag whose capacity is no less than
        the total weight of items in the subset.

        Input: weight/profit = {8, 3, 2}, weight_capacity = [10, 3]
        Output: 13
        8,2 can fit into knapsack with weight capacity 10 and 3 into the one with capacity 3
        """

        if len(capacities) != 2:
            raise ValueError("2 knapsack capacities must be given")
        
        if len(profits) != len(weights):
            raise ValueError("Item value must have corresponding weight")
        
        c1 = capacities[0]
        c2 = capacities[1]
        
        column_len = c1 + 1
        row_len = c2 + 1
        item_len = len(profits)
        size = item_len + 1

        dp = [[[0 for _ in range(column_len)] for _ in range(row_len)] for _ in range(size)]

        # Every element in the first 2D matrix is the base case 0
        for i in range(1, size):
            # Iterate through maximum capacity of bag 2
            for j in range(row_len):
                # Iterate through maximum capacity of bag 1
                for k in range(column_len):
                    current_item_weight, current_item_value = weights[i - 1], profits[i - 1]

                    previous_item = dp[i-1][j][k]

                    # If item can fit in either bag
                    if current_item_weight <= j and current_item_weight <= k:
                        # Find the bag in which it will maximize profit
                        dp[i][j][k] = max(
                            current_item_value + dp[i-1][j - current_item_weight][k],
                            current_item_value + dp[i-1][j][k - current_item_weight],
                            previous_item
                        )
                    # If item can fit in only bag 2
                    elif current_item_weight <= j:
                        dp[i][j][k] = max(
                            current_item_value + dp[i-1][j - current_item_weight][k],
                            previous_item
                        )
                    # If item can fit in only bag 1
                    elif current_item_weight <= k:
                        dp[i][j][k] = max(
                            current_item_value + dp[i-1][j][k - current_item_weight],
                            previous_item
                        )
                    # If item cannot fit at all
                    else:
                        dp[i][j][k] = previous_item

        return dp[item_len][c2][c1]

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 4)
            output = DoubleKnapsack.func(test[0], test[1], test[2])
            self.assertEqual(output, test[3])
