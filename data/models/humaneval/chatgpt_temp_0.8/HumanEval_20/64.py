from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort()  # Sort the numbers in ascending order
    min_diff = float('inf')  # Initialize the minimum difference to infinity
    min_num1 = min_num2 = 0  # Initialize the two numbers with the smallest difference to 0
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i] - numbers[i+1])  # Calculate the absolute difference between adjacent numbers
        if diff < min_diff:  # Check if the current difference is smaller than the current minimum difference
            min_diff = diff
            min_num1 = numbers[i]
            min_num2 = numbers[i+1]
    return (min_num1, min_num2)
