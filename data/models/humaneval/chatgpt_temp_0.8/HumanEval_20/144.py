from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    # sort the numbers in ascending order
    numbers_sorted = sorted(numbers)
    
    # initialize the minimum difference and the corresponding pair of closest elements
    min_diff = float("inf")
    closest_pair = None
    
    # compare adjacent pairs of elements and update the minimum difference and closest pair if needed
    for i in range(len(numbers_sorted) - 1):
        diff = numbers_sorted[i+1] - numbers_sorted[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (numbers_sorted[i], numbers_sorted[i+1])
            
    return closest_pair
