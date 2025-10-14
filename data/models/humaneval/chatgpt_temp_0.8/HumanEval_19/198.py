from typing import List


def sort_numbers(numbers: str) -> str:
    number_dict = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    # Convert the input string into a list of numbers
    number_list = [number_dict[num] for num in numbers.split()]
    # Sort the list of numbers
    sorted_list = sorted(number_list)
    # Convert the sorted list back to a string
    sorted_string = ' '.join([key for key, value in number_dict.items() if value in sorted_list])
    return sorted_string
