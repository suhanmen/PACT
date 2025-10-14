from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort() # sort the list of numbers in ascending order
    min_diff = float('inf') # initialize minimum difference to infinity
    result = (0, 0) # initialize result tuple
    for i in range(len(numbers) - 1): # iterate through the list of numbers
        diff = numbers[i+1] - numbers[i] # calculate difference between adjacent numbers
        if diff < min_diff: # check if current difference is less than current minimum difference
            min_diff = diff # update minimum difference
            result = (numbers[i], numbers[i+1]) # update result tuple with current pair of numbers
    return result # return result tuple
