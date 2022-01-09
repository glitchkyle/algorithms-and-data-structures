class SearchingAlgorithm(object):
    def linearSearch(self, arr, num):
        for i in arr:
            if num == i:
                return True
        return False

    def binarySearch(self, arr, num):
        while True:

            middle = (len(arr) // 2)

            if num == arr[middle]:
                return True

            if(len(arr) <= 1):
                return False
            
            if num < arr[middle]:
                arr = arr[:middle]
            elif num > arr[middle]:
                arr = arr[middle+1:]
        
class SortingAlgorithm(object):
    def bubbleSort(self, arr):
        for count in arr:
            for index in range(len(arr) - 1):
                if arr[index] > arr[index+1]:
                    temp = arr[index]
                    arr[index] = arr[index+1]
                    arr[index+1] = temp
    
    def selectionSort(self, arr):
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
            
    def mergeSort(self, arr):
        if len(arr) > 1:

            # Dividing array by the middle
            mid = len(arr) // 2
            leftArr = arr[:mid]
            rightArr = arr[mid:]

            # Sort each of the divided arrays
            self.mergeSort(leftArr)
            self.mergeSort(rightArr) 

            i = 0 # Index for left array
            j = 0 # Index for right array
            k = 0 # Index for whole array
            
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


            

