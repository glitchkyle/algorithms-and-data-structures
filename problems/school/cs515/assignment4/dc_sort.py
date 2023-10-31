from unittest import TestCase
from statistics import median

def fast_select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]
    
    medians = [median(arr[i:i+5]) for i in range(0, len(arr), 5)]

    pivot = fast_select(medians, len(medians) // 2)

    left = [num for num in arr if num < pivot]
    middle = [num for num in arr if num == pivot]
    right = [num for num in arr if num > pivot]

    if k < len(left):
        return fast_select(left, k)
    elif k < len(left) + len(middle):
        return middle[0]
    else:
        return fast_select(right, k - len(left) - len(middle))

class DivideAndConquerSort(TestCase):

    tests = [
        (
            [23, 5, 17, 10, 3, 9, 12, 8, 19, 14],
            [3, 5, 8, 9, 10, 12, 14, 17, 19, 23]
        ),
        (
            [3, 2, 1],
            [1, 2, 3]
        )
    ]

    @staticmethod
    def func(arr):
        """
        Recall: given an unsorted list A = [a1, a2, ..., an] of size n and an integer k, we can find the kth
        smallest element of A in O(n). Design a sorting algorithm using this idea that sorts A in O(n);
        even if it not possible. What is the complexity of your algorithm you designed?

        O(nlogn) from Master's Theorem
        """
        n = len(arr)

        if n <= 1:
            return arr
        
        pivot = fast_select(arr, n // 2)
        left = [num for num in arr if num < pivot]
        middle = [num for num in arr if num == pivot]
        right = [num for num in arr if num > pivot]

        return DivideAndConquerSort.func(left) + middle + DivideAndConquerSort.func(right)
    

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 2)
            output = DivideAndConquerSort.func(test[0])
            self.assertEqual(output, test[1])
