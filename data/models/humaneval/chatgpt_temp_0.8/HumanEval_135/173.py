def can_arrange(arr):
    i = len(arr) - 1
    while i > 0:
        if arr[i-1] >= arr[i]:
            i -= 1
        else:
            return i-1
    return -1
