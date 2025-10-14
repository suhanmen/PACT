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
    
    # initialize left and right pointers
    left = 0
    right = len(arr) - 1
    changes = 0
    
    while left < right:
        # if the elements at the left and right pointers are not the same
        if arr[left] != arr[right]:
            # increment the number of changes needed
            changes += 1
            # choose the smaller of the two elements and change the other element to it
            arr[left] = min(arr[left], arr[right])
            arr[right] = arr[left]
        # move the left and right pointers towards each other
        left += 1
        right -= 1
    
    return changes
