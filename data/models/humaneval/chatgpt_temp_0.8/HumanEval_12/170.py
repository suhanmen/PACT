from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty. """
    if not strings:
        return None
    max_str = strings[0]
    for string in strings:
        if len(string) > len(max_str):
            max_str = string
    for string in strings:
        if len(string) == len(max_str) and string != max_str:
            return max_str
    return max_str
