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
    copy_arr = array.copy() # create a copy of the given array
    sum_first_last = copy_arr[0] + copy_arr[-1] # calculate the sum of first and last elements of the array
    
    if sum_first_last % 2 == 0: # if sum is even, sort in descending order
        copy_arr.sort(reverse=True)
    else: # if sum is odd, sort in ascending order
        copy_arr.sort()

    return copy_arr # return the sorted array
