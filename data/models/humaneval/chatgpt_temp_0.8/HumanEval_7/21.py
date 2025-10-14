from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring """
    matching_strings = []
    for string in strings:
        if substring in string:
            matching_strings.append(string)
    return matching_strings


