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
    sorted_array = array.copy() # make a copy of the array to avoid changing the original array
    if len(sorted_array) < 2: # if the array has 0 or 1 elements, it is already sorted
        return sorted_array
    sum_of_ends = sorted_array[0] + sorted_array[-1] # sum of first and last elements
    if sum_of_ends % 2 == 0: # even sum means sort in descending order
        sorted_array.sort(reverse=True)
    else: # odd sum means sort in ascending order
        sorted_array.sort()
    return sorted_array
