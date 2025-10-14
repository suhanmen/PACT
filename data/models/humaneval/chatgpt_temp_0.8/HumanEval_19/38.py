python
from typing import List


def sort_numbers(numbers: str) -> str:
    num_dict = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    
    # split the input string into a list of numbers and sort them
    num_list = sorted(numbers.split(), key=lambda x: num_dict[x])
    
    # join the list back into a string and return it
    return ' '.join(num_list)
