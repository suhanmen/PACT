from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Initialize the minimum difference between two adjacent numbers as infinity
    min_diff = float('inf')
    # Initialize the closest pair of numbers as None
    closest_pair = None
    # Iterate over the list of numbers
    for i in range(len(sorted_numbers) - 1):
        # Compute the difference between the current number and the next number
        diff = sorted_numbers[i+1] - sorted_numbers[i]
        # If the difference is smaller than the current minimum difference
        if diff < min_diff:
            # Update the minimum difference
            min_diff = diff
            # Update the closest pair of numbers
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
    # Return the closest pair of numbers
    return closest_pair
