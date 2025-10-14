python
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Initialize the minimum difference between two adjacent elements to infinity
    min_diff = float('inf')
    # Initialize the pair of closest elements to None
    closest_pair = None
    # Iterate over the pairs of adjacent elements
    for i in range(len(sorted_numbers) - 1):
        # Compute the absolute difference between the two elements
        diff = abs(sorted_numbers[i] - sorted_numbers[i+1])
        # If the difference is smaller than the current minimum, update the minimum and the closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
    # Return the closest pair
    return closest_pair
