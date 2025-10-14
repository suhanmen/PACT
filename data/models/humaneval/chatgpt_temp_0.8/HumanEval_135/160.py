def can_arrange(arr):
    n = len(arr)
    ans = -1
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            ans = i-1
    return ans
