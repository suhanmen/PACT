from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None

    longest_str = strings[0]
    for string in strings:
        if len(string) > len(longest_str):
            longest_str = string

    for string in strings:
        if len(string) == len(longest_str) and string != longest_str:
            return longest_str

    return longest_str
