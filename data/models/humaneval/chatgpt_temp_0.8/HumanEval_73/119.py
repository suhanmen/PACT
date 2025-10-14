def smallest_change(arr):
    # Initialize a variable to keep track of the number of elements to change
    num_changes = 0
    
    # Loop through the first half of the array
    for i in range(len(arr)//2):
        # If the current element does not match its reflection, increment num_changes
        if arr[i] != arr[-i-1]:
            num_changes += 1
    
    return num_changes
