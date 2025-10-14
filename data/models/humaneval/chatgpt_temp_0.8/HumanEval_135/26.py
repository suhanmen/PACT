def can_arrange(arr):
    n = len(arr)
    i = n - 1
    while i > 0:
        if arr[i] < arr[i-1]:
            return i - 1
        i -= 1
    return -1
