from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list of numbers in ascending order
    sorted_numbers = sorted(numbers)
    
    # Initialize the minimum difference and the indices of the closest elements
    min_diff = float('inf')
    closest_indices = (0, 0)
    
    # Loop through the adjacent pairs of numbers and update the minimum difference and closest indices
    for i in range(len(sorted_numbers) - 1):
        diff = sorted_numbers[i+1] - sorted_numbers[i]
        if diff < min_diff:
            min_diff = diff
            closest_indices = (i, i+1)
    
    # Return the closest elements in order
    return sorted_numbers[closest_indices[0]], sorted_numbers[closest_indices[1]]
