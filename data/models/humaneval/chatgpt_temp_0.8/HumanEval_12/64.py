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
    if not strings:  # If input list is empty, return None
        return None

    longest_string = strings[0]  # Initialize longest string to be first string in list
    for string in strings:
        if len(string) > len(longest_string):  # If current string is longer than current longest string, update longest string
            longest_string = string
    return longest_string
