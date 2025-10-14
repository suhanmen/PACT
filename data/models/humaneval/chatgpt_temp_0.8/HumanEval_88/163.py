python
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
    arr_copy = array.copy()  # make a copy of the given array so that we don't modify it

    # check if sum of first and last elements is odd or even
    if (arr_copy and arr_copy[0] + arr_copy[-1]) % 2 == 1:
        arr_copy.sort()  # sort the copy in ascending order
    else:
        arr_copy.sort(reverse=True)  # sort the copy in descending order

    return arr_copy
