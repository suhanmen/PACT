from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # sort the list in ascending order
    sorted_numbers = sorted(numbers)
    
    # initialize variables to keep track of the closest pair and their distance
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    min_distance = abs(sorted_numbers[1] - sorted_numbers[0])
    
    # loop through the sorted list and update the closest pair and distance as needed
    for i in range(len(sorted_numbers) - 1):
        current_distance = abs(sorted_numbers[i+1] - sorted_numbers[i])
        if current_distance < min_distance:
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
            min_distance = current_distance
    
    return closest_pair
