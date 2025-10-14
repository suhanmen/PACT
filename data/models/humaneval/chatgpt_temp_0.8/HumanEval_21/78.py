from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Find the minimum and maximum values in the list
    min_val = min(numbers)
    max_val = max(numbers)
    
    # Compute the range of the list
    range_val = max_val - min_val
    
    # Apply the linear transformation to each element of the list
    rescaled_numbers = []
    for num in numbers:
        rescaled_num = (num - min_val) / range_val
        rescaled_numbers.append(rescaled_num)
        
    return rescaled_numbers
