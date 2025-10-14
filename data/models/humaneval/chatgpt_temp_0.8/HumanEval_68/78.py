def pluck(arr):
    # Check if the array is empty
    if not arr:
        return []

    # Initialize variables for the smallest even value and its index
    smallest_even_value = float('inf')
    smallest_even_index = float('inf')

    # Iterate through the array
    for i, val in enumerate(arr):
        # Check if the value is even
        if val % 2 == 0:
            # Check if the even value is smaller than the current smallest even value
            if val < smallest_even_value:
                smallest_even_value = val
                smallest_even_index = i
            # Check if the even value is equal to the current smallest even value but the index is smaller
            elif val == smallest_even_value and i < smallest_even_index:
                smallest_even_index = i

    # Check if we found an even value
    if smallest_even_value == float('inf'):
        return []
    else:
        return [smallest_even_value, smallest_even_index]
