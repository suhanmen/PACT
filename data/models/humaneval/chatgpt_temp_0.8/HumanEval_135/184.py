def can_arrange(arr):
    max_idx = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            max_idx = i-1
    return max_idx
