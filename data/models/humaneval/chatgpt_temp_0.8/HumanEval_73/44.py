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
    # Initialize a counter to keep track of the number of elements that need to be changed
    change_counter = 0
    
    # Loop through the first half of the array
    for i in range(len(arr) // 2):
        # Compare the element at the current index with the corresponding element at the end of the array
        if arr[i] != arr[-i-1]:
            # Increment the counter if the elements are different
            change_counter += 1
    
    # Return the final value of the change counter
    return change_counter
