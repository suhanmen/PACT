from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_length = len(strings[0])
    longest_string = strings[0]
    for string in strings[1:]:
        if len(string) > max_length:
            max_length = len(string)
            longest_string = string
    return longest_string
