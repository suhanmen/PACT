from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)

    # Initialize variables to keep track of the closest pair of numbers
    closest_pair = (sorted_numbers[0], sorted_numbers[1])
    smallest_difference = abs(sorted_numbers[1] - sorted_numbers[0])

    # Iterate over pairs of adjacent numbers in the sorted list
    for i in range(len(sorted_numbers) - 1):
        current_pair = (sorted_numbers[i], sorted_numbers[i+1])
        current_difference = abs(current_pair[1] - current_pair[0])
        if current_difference < smallest_difference:
            closest_pair = current_pair
            smallest_difference = current_difference

    # Return the closest pair of numbers in order (smaller number, larger number)
    return tuple(sorted(closest_pair))
