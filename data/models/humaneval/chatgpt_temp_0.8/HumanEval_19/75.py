from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Define a dictionary to map number names to their corresponding digits
    digit_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}

    # Convert the input string to a list of number names
    number_list = numbers.split()

    # Convert the list of number names to a list of digits
    digit_list = [digit_dict[number_name] for number_name in number_list]

    # Sort the list of digits
    sorted_digit_list = sorted(digit_list)

    # Convert the sorted list of digits back to a list of number names
    sorted_number_list = [number_list[digit_list.index(digit)] for digit in sorted_digit_list]

    # Convert the list of number names back to a string and return it
    return ' '.join(sorted_number_list)
