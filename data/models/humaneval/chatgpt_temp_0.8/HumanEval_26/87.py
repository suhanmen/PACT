from typing import List


def remove_duplicates(numbers: List[int]) -> List[int]:
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers
