from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    # loop through every two consecutive elements of input list `numbers'
    for i in range(len(numbers)-1):
        result.append(numbers[i])
        result.append(delimeter)
    # add the last element of the input list to the result
    if numbers:
        result.append(numbers[-1])
    return result
