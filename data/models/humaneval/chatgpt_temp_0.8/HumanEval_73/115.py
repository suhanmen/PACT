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
    # Initialize variables
    left = 0
    right = len(arr) - 1
    changes = 0
    
    # Loop until left and right pointers cross over
    while left < right:
        # If the elements at the left and right pointers are not equal, increase changes
        if arr[left] != arr[right]:
            changes += 1
        # Move the pointers closer to each other
        left += 1
        right -= 1
    
    # Return the total number of changes made
    return changes
