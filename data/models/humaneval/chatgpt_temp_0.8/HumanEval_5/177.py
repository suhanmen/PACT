from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for index, number in enumerate(numbers):
        # Add the current number to the result
        result.append(number)
        # If this is not the last number, add the delimeter to the result
        if index < len(numbers) - 1:
            result.append(delimeter)
    return result
