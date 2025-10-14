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
    if not strings:
        return None
    max_length = len(strings[0])
    max_string = strings[0]
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            max_string = string
    for string in strings:
        if len(string) == max_length and string != max_string:
            return max_string
    return max_string
