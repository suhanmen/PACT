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
    # First, we can check if the array is already palindromic
    if arr == arr[::-1]:
        return 0
    
    # Otherwise, we need to count the number of elements that need to be changed
    # to make the array palindromic. We can do this by comparing the elements at
    # each end of the array, and moving towards the middle until we find a pair
    # of elements that don't match. At this point, we can either change the left
    # or right element to match the other, and we add 1 to our count. We continue
    # this process until the entire array is palindromic.
    
    # Initialize our count
    count = 0
    
    # Initialize our pointers at the beginning and end of the array
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # If the elements at the left and right pointers match, we can move on
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        else:
            # If the elements don't match, we need to change one of
