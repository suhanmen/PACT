def move_one_ball(arr):
    if not arr:
        # if the array is empty, it is already sorted
        return True

    # find the index of the smallest element
    min_idx = arr.index(min(arr))

    # check if the array is already sorted
    if arr == sorted(arr):
        return True

    # check if the array can be sorted by performing at most one right shift
    shifted_arr = arr[-1:] + arr[:-1]
    if shifted_arr == sorted(shifted_arr):
        return True

    # check if the array can be sorted by performing at most two right shifts
    shifted_arr = shifted_arr[-1:] + shifted_arr[:-1]
    if shifted_arr[:min_idx] == sorted(shifted_arr)[:min_idx] and \
       shifted_arr[min_idx:] == sorted(shifted_arr)[min_idx:]:
        return True

    # it is not possible to sort the array by performing any number of right shifts
    return False
