from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
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
    
    # Split the string into a list of words
    words = numbers.split()
    
    # Convert each word to its corresponding number
    numbers_list = [number_dict[word] for word in words]
    
    # Sort the numbers in ascending order
    sorted_numbers = sorted(numbers_list)
    
    # Convert the sorted numbers back to their corresponding words
    sorted_words = [key for key, value in number_dict.items() if value in sorted_numbers]
    
    # Join the sorted words back into a string
    sorted_string = ' '.join(sorted_words)
    
    return sorted_string
