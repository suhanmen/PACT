def move_one_ball(arr):
    if not arr:  # if array is empty
        return True

    # find the index of the minimum element in the array
    min_index = arr.index(min(arr))

    # perform right shift operation until the minimum element is at the start of the array
    while min_index > 0:
        arr = [arr[-1]] + arr[:-1]  # right shift
        min_index -= 1

    # check if array is sorted in non-decreasing order
    return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
