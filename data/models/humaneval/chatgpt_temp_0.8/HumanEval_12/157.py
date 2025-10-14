from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    longest_str = None
    max_length = 0
    
    for string in strings:
        if len(string) > max_length:
            longest_str = string
            max_length = len(string)
        elif len(string) == max_length:
            longest_str = longest_str if longest_str is not None else string
    
    return longest_str
