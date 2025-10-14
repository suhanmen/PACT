def smallest_change(arr):
    # Initialize counter for number of changes needed
    num_changes = 0
    
    # Check if the array is already palindromic
    if arr == arr[::-1]:
        return 0
    
    # Loop through half of the array and compare elements
    for i in range(len(arr) // 2):
        # If the elements don't match, increment the counter
        if arr[i] != arr[-(i+1)]:
            num_changes += 1
    
    return num_changes
