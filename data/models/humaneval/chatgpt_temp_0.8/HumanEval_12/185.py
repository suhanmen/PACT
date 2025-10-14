from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:  # check if the input list is empty
        return None
    max_len = max(len(s) for s in strings)  # get the length of the longest string
    longest_strings = [s for s in strings if len(s) == max_len]  # get all the strings with the longest length
    return longest_strings[0]  # return the first string in the list of longest strings
