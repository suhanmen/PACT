python
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if in given list of numbers, are any two numbers closer to each other than
    given threshold."""
    for i, num1 in enumerate(numbers):
        for j, num2 in enumerate(numbers[i+1:], start=i+1):
            if abs(num1 - num2) < threshold:
                return True
    return False

