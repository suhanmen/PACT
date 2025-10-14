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
    # Initialize two pointers i and j at the beginning and end of the array
    i, j = 0, len(arr) - 1
    # Initialize a counter to keep track of the number of changes needed
    count = 0
    # While i is less than j, check if arr[i] and arr[j] are equal
    while i < j:
        # If they are not equal, increment count by 1 and update arr[i] or arr[j] to make them equal
        if arr[i] != arr[j]:
            count += 1
            if arr[i] < arr[j]:
                arr[i] = arr[j]
            else:
                arr[j] = arr[i]
        # Move the pointers towards each other
        i += 1
        j -= 1
    # Return the count of changes needed
    return count
