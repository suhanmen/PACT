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
    # Create a copy of the given array
    sorted_array = array.copy()

    # Find the sum of the first and last element of the array
    array_sum = sorted_array[0] + sorted_array[-1]

    # Sort the array in ascending order if array_sum is odd, otherwise sort it in descending order
    if array_sum % 2 != 0:
        sorted_array.sort()
    else:
        sorted_array.sort(reverse=True)

    return sorted_array
