from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # initialize variables to keep track of the closest pair
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    min_distance = abs(sorted_numbers[1] - sorted_numbers[0])
    
    # iterate through the list and check each pair
    for i in range(len(sorted_numbers) - 1):
        distance = abs(sorted_numbers[i+1] - sorted_numbers[i])
        if distance < min_distance:
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
            min_distance = distance
            
    return closest_pair
