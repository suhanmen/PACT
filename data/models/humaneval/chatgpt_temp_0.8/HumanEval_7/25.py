from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring """
    filtered_strings = []
    for word in strings:
        if substring in word:
            filtered_strings.append(word)
    return filtered_strings
