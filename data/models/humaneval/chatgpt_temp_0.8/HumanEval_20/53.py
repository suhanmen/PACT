from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the list of numbers in ascending order
    numbers.sort()
    
    # Initialize variables to keep track of the closest pair of numbers
    min_distance = float('inf')
    closest_pair = None
    
    # Iterate through the list of numbers and compare adjacent pairs
    for i in range(len(numbers) - 1):
        distance = numbers[i+1] - numbers[i]
        if distance < min_distance:
            min_distance = distance
            closest_pair = (numbers[i], numbers[i+1])
    
    # Return the closest pair of numbers in order
    return tuple(sorted(closest_pair))
