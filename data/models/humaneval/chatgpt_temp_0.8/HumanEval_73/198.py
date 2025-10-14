def smallest_change(arr):
    """
    Given an array arr of integers, find the minimum number of elements that
    need to be changed to make the array palindromic. A palindromic array is an array that
    is read the same backwards and forwards. In one change, you can change one element to any other element.

    For example:
    smallest_change([1,2,3,5,4,7,9,6]) == 4
    smallest_change([1, 2, 3, 4, 3, 2, 2]) == 1
    smallest_change([1, 2, 3, 2, 1]) == 0
    """
    # initialize a counter for the number of changes needed
    num_changes = 0
    
    # loop through the array from both ends towards the middle
    for i in range(len(arr) // 2):
        if arr[i] != arr[-i - 1]:
            # if the current two elements don't match, increment the counter
            num_changes += 1
    
    return num_changes
