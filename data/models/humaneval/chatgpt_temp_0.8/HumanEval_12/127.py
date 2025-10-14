from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # Check if the list is empty
        return None
    longest_string = strings[0]  # Set the first string as the longest initially
    for string in strings[1:]:  # Loop through the rest of the strings
        if len(string) > len(longest_string):  # If current string is longer than longest so far,
            longest_string = string  # set current string as longest
    return longest_string
