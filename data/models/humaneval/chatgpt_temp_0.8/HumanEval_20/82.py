from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    """
    numbers.sort() # sort the list in ascending order
    closest_pair = (numbers[0], numbers[1]) # initialize closest_pair as the first two elements of the sorted list
    closest_distance = abs(numbers[0] - numbers[1]) # initialize closest_distance as the absolute difference between the first two elements of the sorted list
    for i in range(1, len(numbers) - 1): # loop through the list from the second element to the second to last element
        current_distance = abs(numbers[i] - numbers[i+1]) # calculate the absolute difference between the current element and the next element
        if current_distance < closest_distance: # if the current distance is smaller than the closest distance so far
            closest_pair = (numbers[i], numbers[i+1]) # update closest_pair to be the current pair 
