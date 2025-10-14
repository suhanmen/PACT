from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    
    numbers.sort()  # sort the list to make finding closest elements easier
    
    closest = (numbers[0], numbers[1])  # initialize closest elements to first two in the list
    min_diff = numbers[1] - numbers[0]  # initialize minimum difference to difference between first two elements
    
    for i in range(1, len(numbers)-1):  # iterate from second to second-to-last element
        diff = numbers[i+1] - numbers[i]  # calculate difference between current element and next element
        if diff < min_diff:  # if difference is smaller than current minimum difference
            min_diff = diff  # update minimum difference
            closest = (numbers[i], numbers[i+1])  # update closest elements
    
    return closest  # return closest elements as a tuple
