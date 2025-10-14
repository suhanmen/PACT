python
from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # Sort the numbers in ascending order
    numbers.sort()
    
    # Set the default minimum difference to be the difference between the first two elements
    min_diff = abs(numbers[1] - numbers[0])
    result = (numbers[0], numbers[1])
    
    # Iterate through the list, updating the minimum difference and result as necessary
    for i in range(1, len(numbers) - 1):
        diff = abs(numbers[i+1] - numbers[i])
        if diff < min_diff:
            min_diff = diff
            result = (numbers[i], numbers[i+1])
    
    return result
