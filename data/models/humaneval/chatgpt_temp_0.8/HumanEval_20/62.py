from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()  # Sort the list of numbers in increasing order
    min_diff = float('inf')  # Initialize the minimum difference to infinity
    closest_pair = ()  # Initialize the tuple to store the closest pair of numbers
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]  # Compute the difference between adjacent numbers
        if diff < min_diff:
            min_diff = diff  # Update the minimum difference if a smaller one is found
            closest_pair = (numbers[i], numbers[i+1])  # Update the closest pair of numbers
    return closest_pair
