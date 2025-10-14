from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    for i, num_i in enumerate(numbers):
        for j, num_j in enumerate(numbers[i+1:]):
            if abs(num_i - num_j) < threshold:
                return True
    return False
