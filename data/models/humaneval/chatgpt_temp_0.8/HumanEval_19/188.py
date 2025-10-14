from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """

    # create a dictionary to store the mapping from word to number
    num_dict = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # split the input string into a list of words
    words = numbers.split()

    # create a list of numbers by mapping each word to its corresponding number
    nums = [num_dict[word] for word in words]

    # sort the list of numbers
    sorted_nums = sorted(nums)

    # create a list of words by mapping each number to its corresponding word
    sorted_words = [key for (key, value) in num_dict.items() if value in sorted_nums]

    # join the sorted words into a single string
    sorted_string = ' '.join(sorted_words)

    return sorted_string
