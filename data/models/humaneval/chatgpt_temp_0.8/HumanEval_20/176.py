from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number). """
    numbers = sorted(numbers) # sort the numbers in ascending order
    min_diff = float('inf') # set initial minimum difference to infinity
    closest = (None, None) # set initial closest numbers to None
    for i in range(len(numbers) - 1): # iterate through the list
        diff = numbers[i+1] - numbers[i] # calculate the difference between adjacent numbers
        if diff < min_diff: # check if difference is smaller than current minimum difference
            min_diff = diff # update minimum difference
            closest = (numbers[i], numbers[i+1]) # update closest numbers
    return closest # return the closest numbers in ascending order
