from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize variables to keep track of the closest pair of numbers found so far
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    closest_distance = abs(sorted_numbers[1] - sorted_numbers[0])
    
    # Iterate over all pairs of adjacent numbers in the sorted list and update the closest pair if applicable
    for i in range(len(sorted_numbers) - 1):
        current_pair = (sorted_numbers[i], sorted_numbers[i+1])
        current_distance = abs(current_pair[1] - current_pair[0])
        if current_distance < closest_distance:
            closest_pair = current_pair
            closest_distance = current_distance
    
    # Return the closest pair of numbers found
    return closest_pair
