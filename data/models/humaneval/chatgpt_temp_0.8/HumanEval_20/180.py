from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list in ascending order
    numbers.sort()

    # Initialize variables to keep track of the closest pair of numbers
    closest_pair = (numbers[0], numbers[1])
    smallest_difference = abs(numbers[1] - numbers[0])

    # Iterate over pairs of adjacent numbers and update closest_pair and smallest_difference as needed
    for i in range(len(numbers) - 1):
        difference = abs(numbers[i+1] - numbers[i])
        if difference < smallest_difference:
            closest_pair = (numbers[i], numbers[i+1])
            smallest_difference = difference

    return closest_pair
