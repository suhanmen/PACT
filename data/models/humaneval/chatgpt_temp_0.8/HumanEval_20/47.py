from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort() # First, sort the list in ascending order
    min_diff = float('inf') # Initialize the minimum difference variable to infinity
    closest_pair = None # Initialize the closest pair to None
    for i in range(len(numbers)-1): # Loop through the list of numbers
        diff = numbers[i+1] - numbers[i] # Calculate the difference between two consecutive numbers
        if diff < min_diff: # If the difference is smaller than the current minimum
            min_diff = diff # Update the minimum difference
            closest_pair = (numbers[i], numbers[i+1]) # Update the closest pair
    return closest_pair # Return the closest pair of numbers
