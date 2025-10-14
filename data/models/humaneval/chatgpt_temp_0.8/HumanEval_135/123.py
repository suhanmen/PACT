def can_arrange(arr):
    n = len(arr)
    if n == 1:
        return -1
    index = -1
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            index = i-1
    return index
