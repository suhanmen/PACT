from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain given substring"""
    filtered_strings = []
    for s in strings:
        if substring in s:
            filtered_strings.append(s)
    return filtered_strings
