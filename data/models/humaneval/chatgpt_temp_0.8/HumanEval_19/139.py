from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Create a dictionary to map number words to their corresponding digit
    number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    
    # Convert the input string to a list of number words
    number_list = numbers.split()
    
    # Convert the number words to digits using the dictionary
    digits = [number_dict[number_word] for number_word in number_list]
    
    # Sort the digits in ascending order
    sorted_digits = sorted(digits)
    
    # Convert the sorted digits back to number words using the dictionary
    sorted_number_words = [key for key, value in number_dict.items() if value in sorted_digits]
    
    # Join the sorted number words into a string and return it
    return ' '.join(sorted_number_words)
