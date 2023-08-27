def merge_sort(arr):
    if len(arr) > 1:

        # Dividing array by the middle
        mid = len(arr) // 2
        leftArr = arr[:mid]
        rightArr = arr[mid:]

        # Sort each of the divided arrays
        merge_sort(leftArr)
        merge_sort(rightArr)

        i = 0  # Index for left array
        j = 0  # Index for right array
        k = 0  # Index for whole array

        # Sort numbers into proper place using sliding window pointers
        while i < len(leftArr) and j < len(rightArr):
            if leftArr[i] < rightArr[j]:
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j += 1
            k += 1

        # Assuming the arrays are already sorted, add any leftovers
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1
        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1
