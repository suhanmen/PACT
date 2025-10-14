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
    # Initialize the count variable to 0
    count = 0

    # Loop through the array from both ends
    for i in range(len(arr)//2):
        # If the elements at the two ends of the array are not equal,
        # increment the count variable
        if arr[i] != arr[len(arr)-i-1]:
            count += 1

    # Return the count variable
    return count
