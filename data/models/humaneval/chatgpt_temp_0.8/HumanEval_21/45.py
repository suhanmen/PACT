from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1"""
    
    min_num = min(numbers)
    max_num = max(numbers)
    range_num = max_num - min_num
    
    # If all numbers are the same, return a list of zeros with the same length as numbers
    if range_num == 0:
        return [0.0] * len(numbers)
    
    # Rescale the numbers to the range [0, 1]
    return [(num - min_num) / range_num for num in numbers]
