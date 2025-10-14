from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
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

    # Split the input string into a list of individual numbers
    num_list = numbers.split()

    # Convert the string numbers to integers using the dictionary
    num_list = [num_dict[num_str] for num_str in num_list]

    # Sort the list of numbers
    num_list.sort()

    # Convert the sorted list back to strings using the dictionary
    sorted_numbers = [key for key, value in num_dict.items() if value in num_list]

    # Join the sorted numbers into a string and return it
    return ' '.join(sorted_numbers)
