from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the numbers in ascending order
    numbers.sort()
    
    # Initialize variables to keep track of the closest pair and their difference
    closest_pair = (numbers[0], numbers[1])
    min_diff = abs(numbers[1] - numbers[0])
    
    # Iterate over all adjacent pairs of numbers and update the closest pair if necessary
    for i in range(len(numbers) - 1):
        diff = abs(numbers[i + 1] - numbers[i])
        if diff < min_diff:
            closest_pair = (numbers[i], numbers[i + 1])
            min_diff = diff
    
    # Return the closest pair
    return closest_pair
