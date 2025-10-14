from typing import List


def rescale_to_unit(numbers: List[float]) -> List[float]:
    """ Given list of numbers (of at least two elements), apply a linear transform to that list,
    such that the smallest number will become 0 and the largest will become 1
    >>> rescale_to_unit([1.0, 2.0, 3.0, 4.0, 5.0])
    [0.0, 0.25, 0.5, 0.75, 1.0]
    """
    original_min = min(numbers)
    original_max = max(numbers)
    rescaled_numbers = []
    for number in numbers:
        rescaled_number = (number - original_min) / (original_max - original_min)
        rescaled_numbers.append(rescaled_number)
    return rescaled_numbers
