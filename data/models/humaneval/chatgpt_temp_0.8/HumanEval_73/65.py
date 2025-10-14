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
    # Initialize the left and right pointers
    left, right = 0, len(arr) - 1
    # Initialize the number of changes needed
    changes = 0
    # Loop until the left pointer is greater than or equal to the right pointer
    while left < right:
        # If the left element is not equal to the right element, increment the number of changes
        if arr[left] != arr[right]:
            changes += 1
        # Move the left pointer to the right and the right pointer to the left
        left += 1
        right -= 1
    # Return the number of changes needed to make the array palindromic
    return changes
