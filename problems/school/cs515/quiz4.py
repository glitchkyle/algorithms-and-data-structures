from unittest import TestCase

class TernarySearch(TestCase):

    tests = [
        (
            [1,2,3,4,5,6,7,8,9,10],
            2,
            1
        ),
    ]

    @staticmethod
    def ternarySearch(l, r, key, ar):
        """
        We divide our array into three parts (by taking two mid) and discard two-third of our
        search space at each iteration. Calculate the complexity of your algorithm and compare it with T(n) =
        2clog2n + O(1) = O(log(n)); [binary search complexity].

        Runtime:
        Dividing the array into 2/3 now
        T(n) = T(2n/3) + O(1)
        a = 1
        b = 3/2
        k = 0

        a = b^k => 1 = 1 => O(logb(n))

        => Ternary Search: O(log3/2(n)) = log3/2(2) * O(log2(n))
        => Binary Search: O(log2(n)) = 1 * O(log2(n))
        => Ternary Search grows asymptotically fast as Binary Search but differs by a constant
        """
        if (r >= l):
            mid1 = l + (r - l) //3
            mid2 = r - (r - l) //3
            if (ar[mid1] == key): 
                return mid1
            if (ar[mid2] == key): 
                return mid2
            if (key < ar[mid1]): 
                return TernarySearch.ternarySearch(l, mid1 - 1, key, ar)
            elif (key > ar[mid2]): 
                return TernarySearch.ternarySearch(mid2 + 1, r, key, ar)
            else: 
                return TernarySearch.ternarySearch(mid1 + 1, mid2 - 1, key, ar)
            
        # Key not found
        return -1

    @staticmethod
    def func(arr, target):
        n = len(arr)
        if n == 0:
            return -1
        return TernarySearch.ternarySearch(0, n, target, arr)

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 3)
            output = TernarySearch.func(test[0], test[1])
            self.assertEqual(output, test[2])
