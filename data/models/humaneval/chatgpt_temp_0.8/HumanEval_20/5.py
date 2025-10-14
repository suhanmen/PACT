from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers)
    # Initialize variables to keep track of the closest pair and its distance
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    min_distance = sorted_numbers[1] - sorted_numbers[0]
    # Iterate over the pairs of adjacent numbers
    for i in range(len(sorted_numbers) - 1):
        distance = sorted_numbers[i+1] - sorted_numbers[i]
        # Update the closest pair and its distance if a closer pair is found
        if distance < min_distance:
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
            min_distance = distance
    return closest_pair
