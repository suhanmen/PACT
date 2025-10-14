def sort_array(array):
    arr_copy = array.copy()

    if len(arr_copy) <= 1:
        return arr_copy

    if (arr_copy[0] + arr_copy[-1]) % 2 == 0:
        arr_copy.sort(reverse=True)
    else:
        arr_copy.sort()

    return arr_copy
