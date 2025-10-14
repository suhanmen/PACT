from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # Sort the list in ascending order
    numbers.sort()
    
    # Initialize variables to store the smallest difference and the corresponding indices
    smallest_difference = float('inf')
    indices = (0, 1)
    
    # Iterate over all pairs of adjacent elements
    for i in range(len(numbers) - 1):
        difference = numbers[i + 1] - numbers[i]
        if difference < smallest_difference:
            smallest_difference = difference
            indices = (i, i + 1)
    
    # Return the two closest elements in ascending order
    return numbers[indices[0]], numbers[indices[1]]
