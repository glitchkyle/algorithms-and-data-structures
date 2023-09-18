from unittest import TestCase

class CoinChange(TestCase):

    tests = [
        ([1, 2, 5], 11, 3),
        ([1, 2, 5], 0, -1),
        ([3, 4, 7], 2, -1),
        ([10], 25, -1),
        ([2, 3, 6, 7], 9, 2),
        ([1, 2, 5, 10], 99, 12),
        ([25, 50, 100], 500, 5),
        ([1, 2, 5, 10], 13, 3),
        ([], 20, -1)
    ]

    @staticmethod
    def func(coins, amount):
        """
        Problem 2
        O(m*n), m = amount, n = len(coins)

        Coin Change Problem: You are given coins of different denominations (assume, you have
        unlimited supply of coins for all denominations) and a total amount of money amount.
        Write an algorithm to compute the fewest number of coins that you need to make up that
        amount. If that amount of money cannot be made up of any combination of the coins,
        return -1.

        Input: coins = {1, 2, 5}, amount = 11
        Output: 3
        5 + 5 + 1 = 11
        """

        # Assumptions
        # 1. No negative or zero numbers within the given input amount or coins

        if amount <= 0:
            return -1

        maximum_amount = amount + 1
        coin_len = len(coins)

        # dp[i] is going to store minimum value
        dp = [float('inf') for _ in range(maximum_amount)]
        dp[0] = 0

        for i in range(1, maximum_amount):
            for j in range(coin_len):
                if coins[j] <= i:
                    dp[i] = min(1 + dp[i - coins[j]], dp[i])
        
        for i in range(maximum_amount):
            if dp[i] == float("inf"):
                dp[i] = -1

        return dp[amount]

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 3)
            output = CoinChange.func(test[0], test[1])
            self.assertEqual(output, test[2])
