from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number). """
    
    # Ensure that the input list has at least two elements
    assert len(numbers) >= 2, "Input list must have at least two elements"
    
    # Sort the list in increasing order
    numbers.sort()
    
    # Initialize variables to store the closest pair of numbers and their distance
    closest_pair = (numbers[0], numbers[1])
    min_distance = abs(numbers[1] - numbers[0])
    
    # Iterate through the list to find the closest pair of numbers
    for i in range(len(numbers)-1):
        distance = abs(numbers[i+1] - numbers[i])
        if distance < min_distance:
            closest_pair = (numbers[i], numbers[i+1])
            min_distance = distance
            
    return closest_pair
