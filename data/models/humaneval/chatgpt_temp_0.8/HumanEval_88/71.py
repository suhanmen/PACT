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
    # make a copy of the array
    copy_array = array.copy()

    # get the sum of the first and last index
    sum_first_last = copy_array[0] + copy_array[-1]

    # sort the array in ascending order if sum_first_last is odd
    # otherwise, sort it in descending order
    if sum_first_last % 2 == 1:
        copy_array.sort()
    else:
        copy_array.sort(reverse=True)

    # return the sorted copy of the array
    return copy_array
