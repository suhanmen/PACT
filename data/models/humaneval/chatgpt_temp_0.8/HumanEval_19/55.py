from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # Define the mapping from numberals to integers
    number_mapping = {
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

    # Split the input string into a list of numberals
    numberals = numbers.split()

    # Convert the numberals to integers using the mapping
    numbers = [number_mapping[numeral] for numeral in numberals]

    # Sort the numbers
    sorted_numbers = sorted(numbers)

    # Convert the sorted numbers back to numberals using the mapping
    sorted_numberals = [list(number_mapping.keys())[list(number_mapping.values()).index(number)] for number in sorted_numbers]

    # Join the sorted numberals into a string and return it
    return ' '.join(sorted_numberals)
