from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the list of numbers in ascending order
    numbers.sort()

    # Initialize variables to keep track of the minimum difference and the corresponding indices
    min_diff = float('inf')
    min_indices = (0, 1)

    # Iterate over pairs of adjacent numbers in the sorted list and update the minimum difference if necessary
    for i in range(len(numbers) - 1):
        diff = numbers[i+1] - numbers[i]
        if diff < min_diff:
            min_diff = diff
            min_indices = (i, i+1)

    # Return the pair of numbers corresponding to the minimum difference
    return (numbers[min_indices[0]], numbers[min_indices[1]])
