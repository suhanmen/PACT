from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()  # Sort the list in ascending order
    min_difference = float('inf')  # Initialize the minimum difference as infinity
    closest_pair = None  # Initialize the closest pair as None
    for i in range(len(numbers) - 1):
        difference = abs(numbers[i] - numbers[i + 1])  # Calculate the difference between consecutive numbers
        if difference < min_difference:
            min_difference = difference
            closest_pair = (numbers[i], numbers[i + 1])
    return closest_pair
