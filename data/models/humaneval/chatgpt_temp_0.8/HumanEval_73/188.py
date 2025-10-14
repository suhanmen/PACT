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
    # initialize a counter variable to keep track of number of changes needed
    changes = 0
    
    # loop through the first half of the array and compare to the second half
    for i in range(len(arr)//2):
        if arr[i] != arr[-i-1]:
            changes += 1
    
    # return the number of changes needed
    return changes
