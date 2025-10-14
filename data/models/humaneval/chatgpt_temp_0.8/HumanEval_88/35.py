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
    arr_copy = array.copy() # copy the given array
    first_val = arr_copy[0] # get the first element
    last_val = arr_copy[-1] # get the last element
    if (first_val + last_val) % 2 == 0: # if the sum is even
        arr_copy.sort(reverse=True) # sort in descending order
    else: # if the sum is odd
        arr_copy.sort() # sort in ascending order
    return arr_copy
