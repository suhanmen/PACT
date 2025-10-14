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
    # Initialize count of changes needed
    changes_needed = 0
    # Loop through the array up to half its length
    for i in range(len(arr)//2):
        # Compare the i-th element from the beginning to the i-th element from the end
        if arr[i] != arr[-i-1]:
            # If they're not equal, increment the count of changes needed
            changes_needed += 1
    return changes_needed
