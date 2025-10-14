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
    # Initialize a variable to track the number of changes needed
    num_changes = 0
    # Loop through the first half of the array
    for i in range(len(arr) // 2):
        # If the i-th element and its corresponding element from the end are not the same
        if arr[i] != arr[-i-1]:
            # Increment num_changes by 1
            num_changes += 1
    # Return the final num_changes value
    return num_changes
