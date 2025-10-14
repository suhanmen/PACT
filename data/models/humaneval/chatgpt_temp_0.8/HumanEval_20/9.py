from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """
    numbers.sort() # sort the list of numbers
    closest = float('inf') # set a variable to hold the closest difference
    closest_pair = () # set a variable to hold the closest pair of numbers
    for i in range(len(numbers)-1): # loop over the sorted list of numbers
        diff = abs(numbers[i] - numbers[i+1]) # calculate the difference between adjacent numbers
        if diff < closest: # if the difference is smaller than the current closest difference
            closest = diff # update the closest difference
            closest_pair = (numbers[i], numbers[i+1]) # update the closest pair of numbers
    return closest_pair # return the closest pair of numbers
