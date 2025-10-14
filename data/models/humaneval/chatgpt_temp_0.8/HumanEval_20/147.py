from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()  # Sort the list of numbers in ascending order
    min_diff = float('inf')  # Initialize the minimum difference as infinity
    closest_numbers = ()  # Initialize the tuple of closest numbers

    # Iterate through the list of numbers and compare adjacent pairs
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i+1])  # Calculate the absolute difference between adjacent pairs
        if diff < min_diff:  # If the difference is smaller than the current min_diff
            min_diff = diff  # Update the min_diff
            closest_numbers = (numbers[i], numbers[i+1])  # Update the closest_numbers tuple

    return closest_numbers  # Return the tuple of closest numbers
