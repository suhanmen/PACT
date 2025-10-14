def can_arrange(arr):
    n = len(arr)
    max_bad_index = -1
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            max_bad_index = i-1
    return max_bad_index
