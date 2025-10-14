from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    output = []
    for i in range(len(numbers)):
        output.append(numbers[i])
        if i < len(numbers) - 1:
            output.append(delimeter)
    return output
