def can_arrange(arr):
    # Start searching from the second element
    for i in range(1, len(arr)):
        # If the current element is less than the previous element,
        # return the index of the current element minus one
        if arr[i] < arr[i-1]:
            return i-1
    # If no such element is found, return -1
    return -1
