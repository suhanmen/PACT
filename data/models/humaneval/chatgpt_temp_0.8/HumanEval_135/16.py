def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """

    # Loop through the array starting from index 1
    for i in range(1, len(arr)):
        
        # Check if current element is not greater than or equal to the previous element
        if arr[i] < arr[i-1]:
            # Return the largest index which meets the condition
            return i-1
    
    # If no such element exists, return -1
    return -1
