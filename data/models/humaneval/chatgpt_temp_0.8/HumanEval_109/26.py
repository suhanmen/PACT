def move_one_ball(arr):
    # If the array is empty or has only one element, it is already sorted
    if len(arr) <= 1:
        return True

    # Find the minimum element in the array
    min_idx = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[min_idx]:
            min_idx = i

    # Check if the array is already sorted in non-decreasing order
    sorted_arr = sorted(arr)
    if arr == sorted_arr:
        return True

    # Check if the array can be sorted by performing right shift operations
    for i in range(1, len(arr)):
        # Shift the array to the right by one position
        arr = [arr[-1]] + arr[:-1]
        # If the minimum element is now at the front of the array, the array can be sorted
        if arr[0] == sorted_arr[min_idx]:
            return True

    # If we couldn't sort the array by performing right shift operations, return False
    return False
