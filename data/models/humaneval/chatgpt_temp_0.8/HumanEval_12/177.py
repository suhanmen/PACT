from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty. """
    
    if not strings: # Return None if input list is empty
        return None
    
    longest_str = strings[0]
    
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string
        elif len(string) == len(longest_str) and string != longest_str:
            # If there's a tie, return the first one
            continue
            
    return longest_str
