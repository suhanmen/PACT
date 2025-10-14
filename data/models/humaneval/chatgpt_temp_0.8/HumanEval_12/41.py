from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty. """
    
    if not strings: # empty list case
        return None
    
    max_length = max(len(string) for string in strings)
    longest_strings = [string for string in strings if len(string) == max_length]
    
    return longest_strings[0]
