def can_arrange(arr):
    n = len(arr)
    i = n - 2
    while i >= 0 and arr[i] < arr[i+1]:
        i -= 1
    return i
