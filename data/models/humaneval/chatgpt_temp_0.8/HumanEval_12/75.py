from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty. """
    
    if not strings:
        return None
    max_len = 0
    longest_str = ""
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            longest_str = string
    for string in strings:
        if len(string) == max_len and string != longest_str:
            return longest_str
    return longest_str
