from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])

    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """
    if not strings:  # If the input list is empty
        return None

    max_len = len(strings[0])  # Initialize the max length to the length of first string
    longest_string = strings[0]  # Initialize the longest string to the first string

    for string in strings[1:]:  # Iterate through remaining strings starting from the second one
        if len(string) > max_len:  # If the current string is longer than the max length
            max_len = len(string)  # Update the max length
            longest_string = string  # Set the longest string to the current string
        elif len(string) == max_len:  # If the current string has the same length as the max length
            longest_string = min(longest_string, string)  # Choose the lexicographically smaller one

    return longest_string
