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

class CircularBinarySearch(TestCase):

    tests = tests = [
        (
            [8, 9, 10, 2, 5, 6],
            10,
            2
        ),
        (
            [8, 9, 10, 2, 5, 6],
            8,
            0
        ),
        (
            [8, 9, 10, 2, 5, 6],
            5,
            4
        ),
        (
            [8, 9, 10, 2, 5, 6],
            3,
            -1
        ),
        (
            [9, 10, 2, 5, 6, 8],
            5,
            3
        ),
        (
            [9, 10, 2, 5, 6, 8],
            9,
            0
        ),
        (
            [9, 10, 2, 5, 6, 8],
            8,
            5
        ),
        (
            [9, 10, 2, 5, 6, 8],
            3,
            -1
        ),
        (
            [3, 4, 5, 6, 7, 1, 2],
            6,
            3
        ),
        (
            [3, 4, 5, 6, 7, 1, 2],
            8,
            -1
        )
    ]

    @staticmethod
    def func(arr, target):
        """
        Search an element in a circularly sorted array: Given a circularly sorted integer array, search
        an element in it. Assume there are no duplicates in the array, and the rotation is in the anti-
        clockwise direction.

        O(logn)
        """
        left = 0
        right = len(arr)-1
        mid = (right + left)//2

        while left <= right:
            if arr[mid] == target:
                return mid
            if arr[mid]<arr[right]:
                if arr[mid]<target<=arr[right]:
                    left = mid+1
                else:
                    right = mid -1
            else:
                if arr[left]<=target<arr[mid]:
                    right = mid
                else:
                    left = mid+1

            mid = (right + left)//2
        return -1
    

    def test(self):
        for test in self.tests:
            self.assertEqual(len(test), 3)
            output = CircularBinarySearch.func(test[0], test[1])
            self.assertEqual(output, test[2])
