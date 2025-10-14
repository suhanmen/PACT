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
    # Initialize a counter to keep track of the number of changes needed
    changes_needed = 0

    # Loop through the first half of the array
    for i in range(len(arr) // 2):
        # If the i-th element from the start is not equal to the i-th element from the end
        if arr[i] != arr[-i - 1]:
            # Increment the changes needed counter
            changes_needed += 1
            # Set the i-th element from the start equal to the i-th element from the end
            arr[i] = arr[-i - 1]

    # Return the changes needed counter
    return changes_needed
