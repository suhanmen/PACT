from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # Check if the list is empty
        return None
    longest_string = strings[0]  # Assume the first string is the longest
    for string in strings[1:]:
        if len(string) > len(longest_string):  # Check if the current string is longer
            longest_string = string
    return longest_string
