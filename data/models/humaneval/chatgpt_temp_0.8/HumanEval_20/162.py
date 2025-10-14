from typing import List, Tuple


def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number)."""
    
    # sort the list of numbers in ascending order
    sorted_nums = sorted(numbers)
    
    # initialize minimum difference to a large number
    min_diff = float('inf')
    
    # initialize variables to store the pair of closest elements
    closest_pair = (0.0, 0.0)
    
    # iterate over the list of numbers and find the pair with the minimum difference
    for i in range(len(sorted_nums) - 1):
        diff = sorted_nums[i+1] - sorted_nums[i]
        if diff < min_diff:
            min_diff = diff
            closest_pair = (sorted_nums[i], sorted_nums[i+1])
    
    return closest_pair

