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
        return None  # Return None if input list is empty
    
    longest_str = strings[0]  # Initialize longest_str to first string in list
    
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string
        elif len(string) == len(longest_str):
            longest_str = min(string, longest_str)
            
    return longest_str
