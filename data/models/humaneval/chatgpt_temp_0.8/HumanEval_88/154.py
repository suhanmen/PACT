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
    # Make a copy of the given array
    arr_copy = array.copy()
    
    # Determine if the sum of the first and last values is odd or even
    if (arr_copy and arr_copy[0] + arr_copy[-1]) % 2 == 0:
        # Sort in descending order if even
        arr_copy.sort(reverse=True)
    else:
        # Sort in ascending order if odd
        arr_copy.sort()
        
    return arr_copy
