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
    # split the input string into a list of words
    words = numbers.split()
    # convert each word to its corresponding number, and sort the list
    nums = sorted([num_dict[word] for word in words])
    # convert the sorted numbers back to words
    sorted_words = [key for key, value in num_dict.items() if value in nums]
    # join the sorted words into a string and return it
    return ' '.join(sorted_words)
