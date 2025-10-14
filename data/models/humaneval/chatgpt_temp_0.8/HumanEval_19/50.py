from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    # Split string by spaces to convert to list of words
    num_words = numbers.split()
    # Convert words to corresponding numbers
    num_list = [number_dict[word] for word in num_words]
    # Sort the list of numbers
    num_list.sort()
    # Convert numbers back to corresponding words
    sorted_words = [key for key, value in number_dict.items() if value in num_list]
    # Join words into a string, separated by spaces
    sorted_numbers = ' '.join(sorted_words)
    return sorted_numbers
