def smallest_change(arr):
    n = len(arr)
    changes = 0
    for i in range(n // 2):
        if arr[i] != arr[n - i - 1]:
            changes += 1
    return changes
