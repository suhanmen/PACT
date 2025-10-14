from typing import List


def sort_numbers(numbers: str) -> str:
    num_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    num_list = [num_dict[num] for num in numbers.split()]
    num_list.sort()
    num_str_list = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in num_list]
    return ' '.join(num_str_list)
