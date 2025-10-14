def sort_array(array):
    # make a copy of the array to avoid modifying the original
    copy = array.copy()
    # determine if the sum of first and last index is odd or even
    sum_first_last = copy[0] + copy[-1]
    is_odd = sum_first_last % 2 == 1
    # sort the copy in ascending or descending order
    if is_odd:
        copy.sort()
    else:
        copy.sort(reverse=True)
    return copy
