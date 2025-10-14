def add_elements(arr, k):
    total = 0
    for i in range(k):
        if abs(arr[i]) < 100:
            total += arr[i]
    return total
