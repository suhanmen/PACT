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
    closest_pair = (numbers[0], numbers[1]) # initialize the closest pair
    min_distance = abs(numbers[1] - numbers[0]) # initialize the minimum distance
    
    for i in range(1, len(numbers) - 1): # iterate over the list from index 1 to second-to-last index
        curr_distance = abs(numbers[i+1] - numbers[i]) # calculate the distance between the current pair of elements
        if curr_distance < min_distance: # if the current distance is smaller than the minimum distance
            min_distance = curr_distance # update the minimum distance
            closest_pair = (numbers[i], numbers[i+1]) # update the closest pair
    
    return closest_pair # return the closest pair
