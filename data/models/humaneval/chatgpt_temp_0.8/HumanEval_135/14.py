def can_arrange(arr):
    prev = arr[0]
    index = -1
    for i in range(1, len(arr)):
        if arr[i] < prev:
            index = i - 1
        else:
            prev = arr[i]
    return index
