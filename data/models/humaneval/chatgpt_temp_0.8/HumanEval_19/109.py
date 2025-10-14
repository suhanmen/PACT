from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    # Split the input string into a list of number words and convert to integers using the number_dict
    numbers_list = [number_dict[num] for num in numbers.split()]
    # Sort the list of integers
    numbers_list.sort()
    # Convert the sorted list of integers back to number words using the number_dict
    sorted_numbers = [list(number_dict.keys())[list(number_dict.values()).index(num)] for num in numbers_list]
    # Join the sorted number words back into a string and return it
    return " ".join(sorted_numbers)
