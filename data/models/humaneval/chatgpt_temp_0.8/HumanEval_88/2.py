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
    copy_array = array.copy()  # create a copy of the array to sort

    if len(copy_array) <= 1:  # if the array has 0 or 1 element, it is already sorted
        return copy_array

    first_element = copy_array[0]  # get the first element
    last_element = copy_array[-1]  # get the last element

    if (first_element + last_element) % 2 == 0:  # if the sum is even, sort in descending order
        copy_array.sort(reverse=True)
    else:  # if the sum is odd, sort in ascending order
        copy_array.sort()

    return copy_array  # return the sorted copy of the array
