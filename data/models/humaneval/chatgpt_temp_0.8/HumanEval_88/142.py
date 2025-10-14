def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """

    copy_array = array.copy() # make a copy of the given array so that we don't modify it
    if len(copy_array) < 2: # if the array has only one or no elements, it is already sorted
        return copy_array
    first = copy_array[0] # first element
    last = copy_array[-1] # last element
    if (first + last) % 2 == 1: # if the sum of first and last is odd
        return sorted(copy_array) # sort in ascending order
    else:
        return sorted(copy_array, reverse=True) # sort in descending order
