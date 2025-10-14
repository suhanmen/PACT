from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings: # Check if the list is empty
        return None
    max_len = 0 # Initialize maximum length to 0
    max_str = '' # Initialize string with maximum length to an empty string
    for s in strings:
        if len(s) > max_len: # Update maximum length and string if current string is longer
            max_len = len(s)
            max_str = s
    return max_str
