from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map numberals to their corresponding integer values
    number_dict = {
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

    # Split the input string into individual numberals and convert them to integers
    numbers_list = [number_dict[numeral] for numeral in numbers.split()]

    # Sort the list of integers
    numbers_list.sort()

    # Convert the sorted list of integers back to numberals
    sorted_numbers = [key for key, value in number_dict.items() if value in numbers_list]

    # Join the sorted numberals back into a string
    sorted_numbers_string = ' '.join(sorted_numbers)

    return sorted_numbers_string
