from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort() # sort the list in ascending order
    closest = float("inf") # initialize closest to infinity
    closest_pair = None # initialize closest pair to None
    
    for i in range(len(numbers)-1):
        if abs(numbers[i] - numbers[i+1]) < closest:
            closest = abs(numbers[i] - numbers[i+1])
            closest_pair = (numbers[i], numbers[i+1])
            
    return closest_pair
