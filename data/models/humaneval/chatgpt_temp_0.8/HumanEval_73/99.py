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
    n = len(arr)
    changes = 0
    
    # Check if the array is already palindromic
    if arr == arr[::-1]:
        return 0
    
    # Iterate over the first half of the array
    for i in range(n // 2):
        # Check if the elements at opposite positions are different
        if arr[i] != arr[n - i - 1]:
            # Increment the number of changes needed
            changes += 1
            # Update the element at the current position with the minimum of the two opposite elements
            arr[i] = arr[n - i - 1] = min(arr[i], arr[n - i - 1])
            
    # Return the total number of changes needed
    return changes
