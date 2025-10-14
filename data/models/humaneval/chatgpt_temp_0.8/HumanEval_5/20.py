from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    interspersed_numbers = []
    for i in range(len(numbers)-1):
        interspersed_numbers.append(numbers[i])
        interspersed_numbers.append(delimeter)
    if len(numbers) > 0:
        interspersed_numbers.append(numbers[-1])
    return interspersed_numbers
