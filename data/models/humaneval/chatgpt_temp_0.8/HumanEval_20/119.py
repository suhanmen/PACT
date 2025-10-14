from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Initialize the minimum difference to be the difference between the first two numbers
    min_diff = abs(sorted_numbers[0] - sorted_numbers[1])
    # Initialize the closest pair to be the first two numbers
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    # Iterate over the rest of the numbers
    for i in range(1, len(sorted_numbers) - 1):
        # Calculate the difference between the current number and the next number
        diff = abs(sorted_numbers[i] - sorted_numbers[i+1])
        # If the difference is smaller than the minimum difference, update the minimum difference and closest pair
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
    return closest_pair
