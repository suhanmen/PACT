from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    # Return None if the input list is empty
    if not strings:
        return None

    # Initialize the longest string to the first string in the list
    longest_str = strings[0]

    # Iterate over the rest of the strings in the list
    for string in strings[1:]:
        # If the current string is longer than the current longest string, update the longest string
        if len(string) > len(longest_str):
            longest_str = string
        # If the current string has the same length as the current longest string, update the longest string
        # if the current string appears earlier in the list
        elif len(string) == len(longest_str) and strings.index(string) < strings.index(longest_str):
            longest_str = string

    return longest_str
