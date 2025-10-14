from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # sort the list in ascending order
    sorted_numbers = sorted(numbers)
    # initialize variables to hold the closest pair of elements and their difference
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    min_difference = abs(sorted_numbers[0] - sorted_numbers[1])
    # iterate through the sorted list and update the closest pair if a smaller difference is found
    for i in range(1, len(sorted_numbers) - 1):
        difference = abs(sorted_numbers[i] - sorted_numbers[i+1])
        if difference < min_difference:
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
            min_difference = difference
    return closest_pair
