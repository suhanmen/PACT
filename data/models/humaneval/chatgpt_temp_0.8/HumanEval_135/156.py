def can_arrange(arr):
    # Initialize the largest index to -1
    largest_index = -1
    # Iterate through the array from the second element to the end
    for i in range(1, len(arr)):
        # Check if the current element is smaller than the previous element
        if arr[i] < arr[i-1]:
            # Update the largest index if the current index is larger
            # than the current largest index
            if i > largest_index:
                largest_index = i
    # Return the largest index
    return largest_index
