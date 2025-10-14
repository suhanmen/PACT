from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the input list in ascending order
    numbers = sorted(numbers)
    # Initialize the minimum difference so far and the corresponding pair of numbers
    min_diff = float('inf')
    min_pair = (0.0, 0.0)
    # Iterate over all adjacent pairs of numbers in the sorted list
    for i in range(len(numbers) - 1):
        # Compute the absolute difference between the current pair of numbers
        diff = abs(numbers[i] - numbers[i+1])
        # Update the minimum difference and the corresponding pair of numbers if necessary
        if diff < min_diff:
            min_diff = diff
            min_pair = (numbers[i], numbers[i+1])
    # Return the pair of numbers with the smallest absolute difference
    return min_pair
