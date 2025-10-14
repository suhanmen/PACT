from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # If the input list is empty, return None.
        return None
    longest_string = strings[0]  # Initialize the longest string as the first element in the list.
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string
