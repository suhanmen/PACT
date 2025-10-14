from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    # sort the input list
    numbers.sort()
    
    # initialize the closest numbers to be the first two elements of the sorted list
    closest = (numbers[0], numbers[1])
    
    # loop through the list and update closest whenever a smaller difference is found
    for i in range(len(numbers)-1):
        diff = numbers[i+1] - numbers[i]
        if diff < closest[1] - closest[0]:
            closest = (numbers[i], numbers[i+1])
    
    return closest
