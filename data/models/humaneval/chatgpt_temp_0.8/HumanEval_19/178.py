from typing import List

NUMERAL_VALUES = {
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
    # Split the input string into a list of numerals
    numerals = numbers.split()

    # Convert each numeral to its integer value and sort the list
    sorted_numerals = sorted(numerals, key=lambda x: NUMERAL_VALUES[x])

    # Convert the sorted numerals back to strings and join them together
    sorted_numbers = ' '.join(sorted_numerals)

    return sorted_numbers
