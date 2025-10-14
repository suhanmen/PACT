def can_arrange(arr):
    # Start iterating from second element and compare with previous element
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            # If current element is less than previous element, return index of previous element
            return i-1
    # If loop completes without finding such element, return -1
    return -1
