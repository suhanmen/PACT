python
def sort_array(array):
    # Make a copy of the original array to avoid modifying it
    arr = array.copy()
    # Determine whether to sort in ascending or descending order
    if (arr and (arr[0] + arr[-1]) % 2 == 1):
        arr.sort()
    else:
        arr.sort(reverse=True)
    return arr
