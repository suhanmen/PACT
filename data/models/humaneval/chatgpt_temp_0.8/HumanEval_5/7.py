# CANNOT PARSE CODE SNIPPET
python
from typing import List


def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    interspersed_numbers = []
    for i, number in enumerate(numbers):
        if i != 0:
            interspersed_numbers.append(delimiter)
        interspersed_numbers.append(number)
    return interspersed_numbers
