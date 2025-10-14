from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """
    From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Initialize the minimum difference and the corresponding pair of numbers
    min_diff = float('inf')
    pair = (None, None)
    # Iterate over adjacent pairs of numbers in the sorted list
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i+1] - sorted_numbers[i]
        # Update the minimum difference and the corresponding pair of numbers if a smaller difference is found
        if diff < min_diff:
            min_diff = diff
            pair = (sorted_numbers[i], sorted_numbers[i+1])
    return pair
