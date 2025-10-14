from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # Convert numbers string to list of integers
    numbers_list = [number_dict[number] for number in numbers.split()]

    # Sort the list of integers
    sorted_numbers = sorted(numbers_list)

    # Convert sorted list of integers back to string of numberals
    sorted_numbers_list = [key for key, value in number_dict.items() if value in sorted_numbers]
    sorted_numbers_string = ' '.join(sorted_numbers_list)

    return sorted_numbers_string
