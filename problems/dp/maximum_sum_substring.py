from copy import deepcopy

def mss(arr):
    sums = [arr[0]]

    for i in range(1, len(arr)):
        if arr[i] + sums[i-1] > arr[i]:
            sums.append(arr[i] + sums[i-1])
        else:
            sums.append(arr[i])

    maximum = max(sums)
    out = deepcopy(arr)
    while sum(out) != maximum:
        out.pop(0)
    return out

def kadane_mss(arr):
    max_ending_here = max_so_far = arr[0]
    start_idx = end_idx = temp_start_idx = 0

    for idx, num in enumerate(arr[1:], start=1):
        if num > max_ending_here + num:
            max_ending_here = num
            temp_start_idx = idx
        else:
            max_ending_here += num

        if max_ending_here > max_so_far:
            max_so_far = max_ending_here
            start_idx = temp_start_idx
            end_idx = idx

    return arr[start_idx:end_idx+1]