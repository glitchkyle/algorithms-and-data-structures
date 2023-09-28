def bubble_sort(arr):
    for _ in range(len(arr)):
        for index in range(len(arr) - 1):
            if arr[index] > arr[index+1]:
                arr[index], arr[index+1] = arr[index+1], arr[index]
