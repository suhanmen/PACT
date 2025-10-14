python
from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Initialize variables to keep track of the two closest numbers and their difference
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    min_diff = abs(sorted_numbers[1] - sorted_numbers[0])
    # Iterate over the sorted list of numbers, comparing adjacent pairs
    for i in range(1, len(sorted_numbers) - 1):
        diff = abs(sorted_numbers[i+1] - sorted_numbers[i])
        # If the current pair of numbers is closer than the current closest pair, update the variables
        if diff < min_diff:
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
            min_diff = diff
    # Return the closest pair of numbers in order (smaller number first)
    return tuple(sorted(closest_pair))
