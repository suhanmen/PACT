def can_arrange(arr):
    # Start from the second last element and move backwards
    for i in range(len(arr)-2, -1, -1):
        # If the current element is smaller than the next element
        if arr[i] < arr[i+1]:
            # Return the index of the current element
            return i
    # If no such element exists, return -1
    return -1
