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
    
    # Initialize counters for left and right indices of array
    left = 0
    right = len(arr) - 1
    
    # Initialize counter for number of changes
    changes = 0
    
    # Loop until left and right indices meet in the middle
    while left < right:
        # If elements at indices don't match, increment changes counter
        if arr[left] != arr[right]:
            changes += 1
        # Move left index one position to the right
        left += 1
        # Move right index one position to the left
        right -= 1
        
    # Retu
