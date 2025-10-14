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
    min_diff = float('inf')  # Initialize the minimum difference to positive infinity
    closest_pair = ()  # Initialize the closest pair tuple
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i+1])  # Calculate the absolute difference between adjacent numbers
        if diff < min_diff:  # If the difference is less than the current minimum difference
            min_diff = diff  # Update the minimum difference
            closest_pair = (numbers[i], numbers[i+1])  # Update the closest pair tuple
    return closest_pair  # Return the two closest numbers as a tuple
