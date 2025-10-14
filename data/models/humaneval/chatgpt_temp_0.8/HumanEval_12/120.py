from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # Return None if the list is empty
        return None
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    for string in strings:
        if len(string) == len(longest_string) and string != longest_string:
            return longest_string  # Return the first longest string in case of multiple ones
    return longest_string
