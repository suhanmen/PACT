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
    # Initialize left and right pointers
    left = 0 
    right = len(arr) - 1 

    # Initialize count of changes required
    count = 0 

    # Loop through the array from left to right and from right to left, comparing elements at each position
    while left < right:
        # If the elements are different, increment the count of changes required
        if arr[left] != arr[right]:
            count += 1
        # Move the pointers towards the center
        left += 1
        right -= 1
      
    # Return the count of changes required
    return count
