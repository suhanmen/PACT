from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty."""
    if len(strings) == 0:
        return None
    longest_str = strings[0]
    for s in strings:
        if len(s) > len(longest_str):
            longest_str = s
    return longest_str
