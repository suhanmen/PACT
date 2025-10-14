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
    copy_array = array.copy() # Create a copy of the given array
    if len(copy_array) == 0: # If the length of the array is zero, return the empty array
        return copy_array
    first_index = copy_array[0] # Get the first index value
    last_index = copy_array[-1] # Get the last index value
    if (first_index + last_index) % 2 == 0: # If the sum of the first and last index values is even
        return sorted(copy_array, reverse=True) # Return the sorted array in descending order
    else:
        return sorted(copy_array) # Return the sorted array in ascending order
