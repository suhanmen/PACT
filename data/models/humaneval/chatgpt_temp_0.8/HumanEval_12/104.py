from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty. """
    
    if len(strings) == 0:
        return None
    
    longest_str = strings[0]
    
    for string in strings[1:]:
        if len(string) > len(longest_str):
            longest_str = string
        elif len(string) == len(longest_str):
            longest_str = min(string, longest_str)
    
    return longest_str
