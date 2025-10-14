from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    interspersed_numbers = []
    for i in range(len(numbers)):
        interspersed_numbers.append(numbers[i])
        if i != len(numbers)-1:
            interspersed_numbers.append(delimeter)
    return interspersed_numbers
