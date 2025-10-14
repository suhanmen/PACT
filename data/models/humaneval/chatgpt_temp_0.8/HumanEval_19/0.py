from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numerals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary that maps each number word to its corresponding integer value
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
    
    # Split the input string into a list of number words
    number_words = numbers.split()
    
    # Convert the list of number words to a list of integers
    numbers_list = [number_dict[word] for word in number_words]
    
    # Sort the list of integers
    sorted_numbers = sorted(numbers_list)
    
    # Convert the sorted list of integers back to a list of number w
