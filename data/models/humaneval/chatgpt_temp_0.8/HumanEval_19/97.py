from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
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
    # Split the input string into a list of numbers
    number_list = numbers.split()
    # Convert the list of numbers to a list of tuples (numberal, numerical value)
    number_tuples = [(number, number_dict[number]) for number in number_list]
    # Sort the list of tuples by the numerical value
    sorted_tuples = sorted(number_tuples, key=lambda x: x[1])
    # Join the sorted list of numberals into a single string
    sorted_numbers = ' '.join([x[0] for x in sorted_tuples])
    return sorted_numbers
