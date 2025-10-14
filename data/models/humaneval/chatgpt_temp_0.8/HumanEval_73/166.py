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
    
    # Initialize two pointers, one from beginning and one from end
    i = 0
    j = len(arr) - 1
    
    # Initialize a counter for the number of changes needed
    count = 0
    
    # Loop until the two pointers meet in the middle
    while i < j:
        
        # If the elements at the two pointers are not the same, increment the counter
        if arr[i] != arr[j]:
            count += 1
            
            # If the element at the start pointer is smaller, change it to the element at the end pointer
            if arr[i] < arr[j]:
                arr[i] = arr[j]
                
            # If the element at the end pointer is smaller, change it to the element at the start pointer
            else:
                arr[j] = arr[i]
                
        # Move the two pointers closer to each other
        i += 1
        j -= 1
        
    # Return the number of changes needed
    return count
