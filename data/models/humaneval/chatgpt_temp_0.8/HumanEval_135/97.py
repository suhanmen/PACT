python
def can_arrange(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):
        if arr[i] < arr[i-1]:
            return i - 1
    return -1
