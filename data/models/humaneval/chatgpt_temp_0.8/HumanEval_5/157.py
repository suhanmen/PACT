from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    # Iterate through the numbers list except for the last element
    for i in range(len(numbers) - 1):
        # Append the current number and the delimiter to the result list
        result.append(numbers[i])
        result.append(delimeter)
    # Append the last number to the result list
    if numbers:
        result.append(numbers[-1])
    return result
