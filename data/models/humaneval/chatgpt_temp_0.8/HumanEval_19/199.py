NUMBER_WORDS = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def sort_numbers(numbers: str) -> str:
    """
    Input is a space-delimited string of numberals from 'zero' to 'nine'.
    Valid choices are 'zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight' and 'nine'.
    Return the string with numbers sorted from smallest to largest.
    >>> sort_numbers('three one five')
    'one three five'
    """
    # Convert string to list of number words
    num_words = numbers.split()

    # Convert number words to integers
    nums = [NUMBER_WORDS.index(word) for word in num_words]

    # Sort the list of integers
    sorted_nums = sorted(nums)

    # Convert sorted integers back to number words
    sorted_words = [NUMBER_WORDS[num] for num in sorted_nums]

    # Join sorted number words into a string and return it
    return ' '.join(sorted_words)
