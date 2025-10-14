from typing import List

number_dict = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Split the input into a list of number strings
    num_list = numbers.split()
    
    # Sort the number strings using their integer values
    sorted_list = sorted(num_list, key=lambda x: number_dict[x])
    
    # Join the sorted number strings into a string
    sorted_str = " ".join(sorted_list)
    
    return sorted_str
