from typing import List


def sort_numbers(numbers: str) -> str:
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
    
    # Split the string into a list of numbers
    num_list = numbers.split()
    
    # Convert each number from string to integer using the dictionary
    num_list = [num_dict[x] for x in num_list]
    
    # Sort the list
    num_list.sort()
    
    # Convert each number from integer to string using the dictionary
    num_list = [list(num_dict.keys())[list(num_dict.values()).index(x)] for x in num_list]
    
    # Join the list back into a string
    sorted_numbers = ' '.join(num_list)
    
    return sorted_numbers
