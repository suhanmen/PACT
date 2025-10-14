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
    # Initialize a variable to keep track of how many elements need to be changed
    num_changes = 0
    
    # Use two pointers to iterate through the array from the beginning and end
    left = 0
    right = len(arr) - 1
    
    # While the pointers haven't crossed each other
    while left <= right:
        # If the elements at the left and right pointers are not equal, increment num_changes
        # and change the smaller element to the larger element
        if arr[left] != arr[right]:
            num_changes += 1
            arr[left] = max(arr[left], arr[right])
            arr[right] = max(arr[left], arr[right])
        # Move the pointers closer to each other
        left += 1
        right -= 1
    
    return num_changes
