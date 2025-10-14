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
    # Initialize a variable to keep track of the number of changes
    num_changes = 0
    # Loop through half of the array
    for i in range(len(arr) // 2):
        # If the element at the current index is not equal to the element at its corresponding index from the end of the array
        if arr[i] != arr[-i-1]:
            # Increment the number of changes
            num_changes += 1
    # Return the total number of changes needed
    return num_changes
