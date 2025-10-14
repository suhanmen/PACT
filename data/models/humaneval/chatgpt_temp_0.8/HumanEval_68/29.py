python
def pluck(arr):
    # Initialize variables for smallest even value and its index
    smallest_val = float('inf')
    smallest_idx = float('inf')
    
    # Loop through the array to find the smallest even value and its index
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] < smallest_val:
            smallest_val = arr[i]
            smallest_idx = i
    
    # If no even values were found, return an empty list
    if smallest_val == float('inf'):
        return []
    
    # Otherwise, return the smallest even value and its index in a list
    return [smallest_val, smallest_idx]
