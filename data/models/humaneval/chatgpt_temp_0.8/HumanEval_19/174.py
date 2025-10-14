from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary of numberals in key-value pairs
    numberals = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    # Split the input string into a list of numberals
    numberal_list = numbers.split()
    
    # Convert each numberal to its numeric representation
    numeric_list = [numberals[x] for x in numberal_list]
    
    # Sort the list of numeric representations
    sorted_list = sorted(numeric_list)
    
    # Convert each numeric representation back to its numberal form
    sorted_numberal_list = [list(numberals.keys())[list(numberals.values()).index(x)] for x in sorted_list]
    
    # Join the sorted numberal list into a string and return it
    return ' '.join(sorted_numberal_list)
