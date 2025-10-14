from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    # Find the smallest and largest numbers in the list
    smallest = min(numbers)
    largest = max(numbers)
    
    # Apply the linear transformation
    transformed_numbers = [(x - smallest) / (largest - smallest) for x in numbers]
    
    return transformed_numbers
