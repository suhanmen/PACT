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
    
    # Initialize variables to keep track of the closest numbers
    closest_numbers = (numbers[0], numbers[1])
    min_difference = abs(numbers[1] - numbers[0])
    
    # Check the difference between adjacent numbers
    for i in range(1, len(numbers)-1):
        difference = abs(numbers[i+1] - numbers[i])
        
        # Update the closest numbers if the difference is smaller
        if difference < min_difference:
            closest_numbers = (numbers[i], numbers[i+1])
            min_difference = difference
    
    return closest_numbers
