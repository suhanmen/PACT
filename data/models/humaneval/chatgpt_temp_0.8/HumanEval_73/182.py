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

    # Initialize pointers to left and right ends of array
    left = 0
    right = len(arr) - 1

    # Initialize variable to keep track of number of changes made
    num_changes = 0

    # Keep looping while left pointer is less than right pointer
    while left < right:
        # If the elements at the left and right pointers are not equal
        if arr[left] != arr[right]:
            # Increment the number of changes made
            num_changes += 1
            # Replace the smaller element with the larger one
            if arr[left] < arr[right]:
                arr[left] = arr[right]
            else:
                arr[right] = arr[left]
        # Move the left and right pointers inwards
        left += 1
        right -= 1

    # Return the total number of changes made
    return num_changes
