def move_one_ball(arr):
    if not arr:  # if the array is empty
        return True

    n = len(arr)
    min_val = min(arr)  # find the minimum value in the array
    min_idx = arr.index(min_val)  # get the index of the minimum value

    # check if the array can be sorted without shifting
    if arr == sorted(arr):
        return True

    # start checking for the possible number of right shifts
    for i in range(1, n):
        idx = (min_idx-i+n) % n
        if arr[idx] >= arr[idx+1:]:
            right_shift = arr[idx+1:] + arr[:idx+1]
            if right_shift == sorted(arr):
                return True
    return False
