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
    # initialize start and end indices
    start = 0
    end = len(arr) - 1
    
    # initialize count of changes
    changes = 0
    
    # loop until start index is greater than or equal to end index
    while start < end:
        # if elements at start and end indices are not equal, increment changes
        if arr[start] != arr[end]:
            changes += 1
        start += 1
        end -= 1
    
    # return count of changes
    return changes
