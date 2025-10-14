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
    # Initialize the number of changes required to 0
    changes_required = 0 

    # Loop through the first half of the array
    for i in range(len(arr) // 2):
        # Check if the element at index i is equal to the element at the opposite end of the array
        if arr[i] != arr[-i - 1]:
            # Increment the number of changes required
            changes_required += 1

    # Return the number of changes required
    return changes_required
