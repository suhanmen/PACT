python
def pluck(arr):
    # Initialize variables to hold the smallest even value and its index
    smallest_even = None
    smallest_even_index = None
    
    # Iterate through the array to find the smallest even value and its index
    for i, value in enumerate(arr):
        if value % 2 == 0 and (smallest_even is None or value < smallest_even):
            smallest_even = value
            smallest_even_index = i
    
    # If no even values were found, return an empty list
    if smallest_even is None:
        return []
    
    # Otherwise, return the smallest even value and its index in a list
    return [smallest_even, smallest_even_index]
