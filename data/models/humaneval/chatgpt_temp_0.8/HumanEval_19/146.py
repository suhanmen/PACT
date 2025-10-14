from typing import List


def sort_numbers(numbers: str) -> str:
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5,
                'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    split_numbers = numbers.split()
    split_numbers.sort(key=lambda x: num_dict[x])
    sorted_numbers = ' '.join(split_numbers)
    return sorted_numbers
