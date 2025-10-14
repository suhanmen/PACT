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
    sorted_array = array.copy() # create a copy of the original array so that we don't modify it
    if len(array) < 2: # if the array has 0 or 1 elements, there is nothing to sort
        return sorted_array
    if (array[0] + array[-1]) % 2 == 0: # if the sum of the first and last elements is even, sort in descending order
        sorted_array.sort(reverse=True)
    else: # if the sum of the first and last elements is odd, sort in ascending order
        sorted_array.sort()
    return sorted_array
