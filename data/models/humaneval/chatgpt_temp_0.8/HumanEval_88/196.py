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
    # create a copy of the original array
    new_array = array.copy()

    # find the sum of the first and last elements in the array
    sum_first_last = new_array[0] + new_array[-1]

    # sort the array in ascending order if the sum is odd, descending order if even
    if sum_first_last % 2 == 0:
        new_array.sort(reverse=True)
    else:
        new_array.sort()

    return new_array
