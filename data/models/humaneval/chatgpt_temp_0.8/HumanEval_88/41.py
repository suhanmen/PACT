def sort_array(array):
    # make a copy of the array to avoid changing the original
    sorted_array = array.copy()
    # determine the sum of the first and last element
    s = array[0] + array[-1]
    # sort the array in ascending or descending order based on the sum
    if s % 2 == 0:
        sorted_array.sort(reverse=True)
    else:
        sorted_array.sort()
    return sorted_array
