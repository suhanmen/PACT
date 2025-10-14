from typing import List


def sort_numbers(numbers: str) -> str:
    """ Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest
    >>> sort_numbers('three one five')
    'one three five'
    """
    # create a dictionary to map words to their numerical equivalent
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
    
    # split the input string into a list of words
    word_list = numbers.split()
    
    # convert each word to its numerical equivalent
    num_list = [num_dict[word] for word in word_list]
    
    # sort the numerical list
    sorted_nums = sorted(num_list)
    
    # convert the sorted numerical list back to words
    sorted_words = [key for key, value in num_dict.items() if value in sorted_nums]
    
    # join the sorted words into a string and return it
    return ' '.join(sorted_words)
