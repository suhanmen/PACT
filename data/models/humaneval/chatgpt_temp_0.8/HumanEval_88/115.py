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
    sorted_array = array.copy() # create a copy of the input array
    if len(sorted_array) <= 1:
        return sorted_array # return the array as is if it has 0 or 1 element
    else:
        first = sorted_array[0] # get the first element of array
        last = sorted_array[-1] # get the last element of array
        if (first + last) % 2 == 0:
            sorted_array.sort(reverse=True) # sort in descending order if sum is even
        else:
            sorted_array.sort() # sort in ascending order if sum is odd
        return sorted_array # return the sorted copy of the input array
