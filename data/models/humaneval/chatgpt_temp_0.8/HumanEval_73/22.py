python
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
    
    # Initialize counter for number of changes
    num_changes = 0
    
    # Loop until left and right pointers meet or cross
    while left < right:
        # If elements at the left and right pointers match, move both pointers inward
        if arr[left] == arr[right]:
            left += 1
            right -= 1
        # If elements do not match, increment number of changes and move left pointer inward
        else:
            num_changes += 1
           
