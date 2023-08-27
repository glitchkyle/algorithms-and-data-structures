def binarySearch(arr, num):
    while True:

        middle = (len(arr) // 2)

        if num == arr[middle]:
            return True

        if (len(arr) <= 1):
            return False

        if num < arr[middle]:
            arr = arr[:middle]
        elif num > arr[middle]:
            arr = arr[middle+1:]
