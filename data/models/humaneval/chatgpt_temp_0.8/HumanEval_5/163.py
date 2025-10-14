from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    output = []
    for i in range(len(numbers)):
        if i != 0:
            output.append(delimeter)
        output.append(numbers[i])
    return output
