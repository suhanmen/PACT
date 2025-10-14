from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map numberals to integers
    numberal_to_int = {
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
    numberal_list = numbers.split()
    
    # Convert each numberal to its corresponding integer using the dictionary
    int_list = [numberal_to_int[numberal] for numberal in numberal_list]
    
    # Sort the integer list
    sorted_int_list = sorted(int_list)
    
    # Convert the sorted integer list back to a list of numberals
    sorted_numberal_list = [key for key, value in numberal_to_int.items() if value in sorted_int_list]
    
    # Join the sorted numberal list into a space-delimited string
    sorted_numbers = ' '.join(sorted_numberal_list)
    
    return sorted_numbers
