def move_one_ball(arr):
    n = len(arr)
    if n == 0:
        return True

    # Find the minimum element and its index
    min_val = min(arr)
    min_idx = arr.index(min_val)

    # Check if the array is already sorted
    if arr == sorted(arr):
        return True

    # Check if the array can be sorted using a single right shift
    if arr[n - 1] <= arr[0] and arr[min_idx - 1] <= arr[min_idx]:
        return True

    # Check if the array can be sorted using multiple right shifts
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            return False

    return True
