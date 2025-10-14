def can_arrange(arr):
    largest_index = -1  # initialize the largest index
    
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            largest_index = i-1  # update largest index if condition is met
    
    return largest_index
