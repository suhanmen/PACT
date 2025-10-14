from typing import List

NUMERALS = {
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


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Convert the string of numberals to a list of integers
    num_list = [NUMERALS[numeral] for numeral in numbers.split()]

    # Sort the list of integers and convert back to a string of numberals
    sorted_num_list = sorted(num_list)
    sorted_numerals = [key for key, value in NUMERALS.items() if value in sorted_num_list]

    return ' '.join(sorted_numerals)
