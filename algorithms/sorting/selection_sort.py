def selection_sort(arr):
    for index in range(len(arr) - 1):

        # Search through for lowest value
        searchIndex = index
        currentVal = arr[index]
        for tempIndex in range(index + 1, len(arr)):
            if arr[tempIndex] < currentVal:
                searchIndex = tempIndex
                currentVal = arr[tempIndex]

        # Switch values
        arr[searchIndex] = arr[index]
        arr[index] = currentVal
