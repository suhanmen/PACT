from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings: # check if the input list is empty
        return None
    longest_string = strings[0]
    for string in strings:
        if len(string) > len(longest_string):
            longest_string = string
    return longest_string
