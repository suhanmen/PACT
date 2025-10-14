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
    array_copy = array.copy()

    # Check if the sum of first and last index is odd or even
    if (array_copy[0] + array_copy[-1]) % 2 == 0:
        # If even, sort the array in descending order
        array_copy.sort(reverse=True)
    else:
        # If odd, sort the array in ascending order
        array_copy.sort()

    # Return the sorted copy of the array
    return array_copy
