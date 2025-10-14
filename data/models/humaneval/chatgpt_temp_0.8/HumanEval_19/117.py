from typing import List

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


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split string into a list of strings
    numbers_list = numbers.split()

    # Convert each string to its corresponding number value
    numbers_list = [number_dict[number_string] for number_string in numbers_list]

    # Sort the list of numbers in ascending order
    numbers_list = sorted(numbers_list)

    # Convert each number back to its corresponding string value and join into a single string
    numbers_sorted = [key for key, value in number_dict.items() if value in numbers_list]
    numbers_sorted_str = " ".join(numbers_sorted)

    return numbers_sorted_str
