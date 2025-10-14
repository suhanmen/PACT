from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list in ascending order
    numbers.sort()
    # Initialize the minimum difference and the corresponding pair of numbers
    min_diff = float('inf')
    closest_pair = (0.0, 0.0)
    # Iterate over the adjacent pairs of numbers and update the minimum difference and closest pair if necessary
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i+1])
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i+1])
    # Return the closest pair
    return closest_pair
