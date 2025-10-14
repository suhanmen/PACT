def pluck(arr):
    # Edge case: empty array
    if not arr:
        return []

    # Initialize variables
    smallest_even = None
    smallest_index = None

    # Loop through array
    for i, val in enumerate(arr):
        # If value is even
        if val % 2 == 0:
            # If smallest_even is not set, or the current value is smaller
            if smallest_even is None or val < smallest_even:
                smallest_even = val
                smallest_index = i
            # If current value is equal to smallest_even and has smaller index
            elif val == smallest_even and i < smallest_index:
                smallest_index = i
    
    # If no even values
    if smallest_even is None:
        return []
    
    # Return smallest even value and its index in a list
    return [smallest_even, smallest_index]
