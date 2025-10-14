from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty."""
    
    if not strings:  # Return None if the list is empty
        return None
    
    max_length = len(strings[0])  # Initialize max_length with the first string's length
    longest_string = strings[0]  # Initialize longest_string with the first string
    
    for string in strings[1:]:  # Loop through the rest of the strings
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
        elif len(string) == max_length and strings.index(string) < strings.index(longest_string):
            longest_string = string
                
    return longest_string
