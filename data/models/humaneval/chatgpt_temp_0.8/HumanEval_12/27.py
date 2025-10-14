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
    if not strings:  # If the list is empty
        return None
    longest_string = strings[0]  # Initialize the longest string to the first string in the list
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string  # If we find a longer string, update the longest string
    return longest_string
