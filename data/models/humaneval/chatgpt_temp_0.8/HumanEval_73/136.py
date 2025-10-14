def smallest_change(arr):
    # Initialize a counter for the number of changes needed
    changes = 0
    
    # Loop over the first half of the array
    for i in range(len(arr) // 2):
        # Compare the current element with its mirror image
        if arr[i] != arr[-i - 1]:
            # Increment the changes counter by 1
            changes += 1
            # Replace the current element with its mirror image
            arr[i] = arr[-i - 1]
    
    # Return the total number of changes needed
    return changes
