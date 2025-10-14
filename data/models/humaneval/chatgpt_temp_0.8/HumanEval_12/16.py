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
    if len(strings) == 0:  # Check if the list is empty
        return None
    longest_string = strings[0]  # Initialize the longest string to the first string
    for string in strings:
        if len(string) > len(longest_string):  # If the current string is longer than the longest string
            longest_string = string  # Set the current string as the longest string
        elif len(string) == len(longest_string) and string != longest_string:  # In case of multiple strings of the same length
            continue  # Skip the current string and keep the previous longest string
    return longest_string
