def can_arrange(arr):
    index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            index = i-1
    return index
