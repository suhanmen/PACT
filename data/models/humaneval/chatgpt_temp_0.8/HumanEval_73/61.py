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
    # Initialize two pointers to the start and end of the array
    i, j = 0, len(arr) - 1
    # Initialize a variable to keep track of the number of changes needed
    changes = 0
    # Loop through the array while the two pointers don't cross each other
    while i < j:
        # If the elements at the two pointers are different, increment the changes variable
        if arr[i] != arr[j]:
            changes += 1
        # Move the pointers towards each other
        i += 1
        j -= 1
    # Return the number of changes needed
    return changes
