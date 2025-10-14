from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # initialize the minimum difference to a large value
    min_difference = sorted_numbers[-1] - sorted_numbers[0]
    
    # initialize the closest pair to be the first and second numbers
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    
    # loop through the sorted numbers, comparing each adjacent pair
    for i in range(len(sorted_numbers) - 1):
        difference = sorted_numbers[i+1] - sorted_numbers[i]
        if difference < min_difference:
            min_difference = difference
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
    
    return closest_pair
