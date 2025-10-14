python
from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring """
    result = []
    for string in strings:
        if substring in string:
            result.append(string)
    return result

