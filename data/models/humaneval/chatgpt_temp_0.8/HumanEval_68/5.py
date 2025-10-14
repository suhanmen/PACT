def pluck(arr):
    # Initialize smallest even value and its index
    smallest_even = float('inf')
    smallest_even_index = -1
    
    # Iterate over each element in the array
    for i in range(len(arr)):
        # Check if element is even and smaller than current smallest even value
        if arr[i] % 2 == 0 and arr[i] < smallest_even:
            smallest_even = arr[i]
            smallest_even_index = i
    
    # If no even value was found, return an empty list
    if smallest_even == float('inf'):
        return []
    
    # Otherwise, return a list with smallest even value and its index
    return [smallest_even, smallest_even_index]
