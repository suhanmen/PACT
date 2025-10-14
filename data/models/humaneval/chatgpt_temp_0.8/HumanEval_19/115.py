from typing import List


def sort_numbers(numbers: str) -> str:
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_list = [num_dict[i] for i in numbers.split()]
    num_list.sort()
    return ' '.join([list(num_dict.keys())[list(num_dict.values()).index(i)] for i in num_list])
