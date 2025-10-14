from typing import List


def sort_numbers(numbers: str) -> str:
    number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    number_list = numbers.split()
    number_list.sort(key=lambda x: number_dict[x])
    return ' '.join(number_list)
