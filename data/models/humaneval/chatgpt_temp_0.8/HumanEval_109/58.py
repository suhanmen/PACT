def move_one_ball(arr):
    # If the given list is empty, return True.
    if not arr:
        return True

    # Find the index where the smallest element is located and store it in min_index.
    min_index = arr.index(min(arr))

    # Shift the array so that the smallest element is at the beginning.
    arr = arr[min_index:] + arr[:min_index]

    # Check if the array is sorted in non-decreasing order.
    for i in range(len(arr) - 1):
        if arr[i] > arr[i+1]:
            return False

    return True
