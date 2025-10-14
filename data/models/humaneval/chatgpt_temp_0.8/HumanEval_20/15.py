from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list to simplify the search for closest elements
    sorted_numbers = sorted(numbers)
    # Initialize variables to keep track of the closest pair found so far
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    closest_distance = abs(sorted_numbers[0] - sorted_numbers[1])
    # Iterate over the list and update the closest pair if a closer pair is found
    for i in range(len(sorted_numbers) - 1):
        distance = abs(sorted_numbers[i] - sorted_numbers[i+1])
        if distance < closest_distance:
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
            closest_distance = distance
    return closest_pair
