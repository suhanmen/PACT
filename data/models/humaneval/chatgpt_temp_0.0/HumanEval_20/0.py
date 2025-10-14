from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the minimum difference and the corresponding pair of numbers
    min_diff = float('inf')
    closest_pair = None
    
    # Iterate over adjacent pairs of numbers in the sorted list
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i+1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_numbers[i], sorted_numbers[i+1])
    
    # Return the closest pair of numbers
    return closest_pair