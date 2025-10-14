from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings: # if the input list is empty
        return None
    longest_str = strings[0] # assume the first string is the longest initially
    for string in strings[1:]: # check the other strings
        if len(string) > len(longest_str): # if found a longer string
            longest_str = string # update the longest string
    return longest_str
