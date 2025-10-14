def smallest_change(arr):
    n = len(arr)
    changes = 0
    for i in range(n // 2):
        j = n - i - 1
        if arr[i] != arr[j]:
            changes += 1
            arr[i] = arr[j] = max(arr[i], arr[j])
    return changes
