from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_length = 0
    longest_string = ""
    for string in strings:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
    for string in strings:
        if len(string) == max_length:
            return string
    return longest_string
