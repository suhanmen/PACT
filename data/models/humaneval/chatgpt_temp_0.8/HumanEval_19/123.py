from typing import List

def sort_numbers(numbers: str) -> str:
    num_map = {
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
    # Convert input string to list of numbers
    num_list = [num_map[word] for word in numbers.split()]
    # Sort list of numbers
    num_list.sort()
    # Convert sorted list of numbers back to string
    sorted_numbers = ' '.join([num_map[num] for num in num_list])
    return sorted_numbers
