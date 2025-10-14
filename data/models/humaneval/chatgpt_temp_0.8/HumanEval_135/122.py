def can_arrange(arr):
    # Initialize the largest index variable as -1
    largest_index = -1

    # Loop through the array, starting from the second element
    for i in range(1, len(arr)):
        # If the current element is smaller than the previous element,
        # update the largest index variable to the previous index
        if arr[i] < arr[i-1]:
            largest_index = i-1

    # Return the largest index variable
    return largest_index
