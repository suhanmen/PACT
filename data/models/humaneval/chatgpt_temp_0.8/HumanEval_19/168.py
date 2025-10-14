from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map numberals to integers
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
    
    # Split the input string into a list of numberals
    num_list = numbers.split()
    
    # Convert each numberal to an integer using the dictionary
    num_ints = [num_dict[num] for num in num_list]
    
    # Sort the integers
    num_ints.sort()
    
    # Convert the integers back to numberals using the dictionary
    sorted_nums = [list(num_dict.keys())[list(num_dict.values()).index(num)] for num in num_ints]
    
    # Join the sorted numberals into a string and return
    return ' '.join(sorted_nums)
