def can_arrange(arr):
    last_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            last_index = i-1
    return last_index
