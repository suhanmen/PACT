from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ Insert a number 'delimeter' between every two consecutive elements of input list `numbers' """
    output = []
    for i in range(len(numbers)):
        output.append(numbers[i])
        if i < len(numbers) - 1:
            output.append(delimeter)
    return output

