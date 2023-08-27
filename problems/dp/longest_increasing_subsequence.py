def lis(arr):

    # First solution
    
    # 5 7 4 -3 9 1 10 4 5 8 9 3
    
    # Choose list with ending number less than current number
    # Choose list with most numbers filled

    # 5(0) 7(1) 9(4) 10(6)
    # 4(2)
    # -3(3) 1(5) 4(7) 5(8) 8(9) 9(10)
    # 3 (11)

    # Optimized solution

    # Associative array of numbers keeping track of length of array

    # 5 7 4 -3 9 1 10 4 5 8 9 3
    # 1 2 1  1 

    size_of_arr = len(arr)

    out = [1] * size_of_arr

    for i in range(1, size_of_arr):
        for j in range(0, i):
            # Add number to L(i) if
            # Less than current number
            # Subsequence with most number filled
            if arr[j] < arr[i] and out[i] < out[j] + 1:
                out[i] = out[j] + 1

    maximum = 1
    for i in out:
        maximum = max(maximum, i)

    return maximum