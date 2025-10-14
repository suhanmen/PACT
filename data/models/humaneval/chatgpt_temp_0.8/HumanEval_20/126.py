from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()  # Sort the list of numbers
    min_diff = float('inf')  # Initialize minimum difference to infinity
    closest_pair = None  # Initialize closest pair to None
    for i in range(len(numbers)-1):
        diff = numbers[i+1] - numbers[i]  # Calculate difference between adjacent elements
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers[i], numbers[i+1])  # Update closest pair if new minimum difference is found
    return closest_pair
