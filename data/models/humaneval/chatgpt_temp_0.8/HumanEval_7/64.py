from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring """
    
    output = []
    for s in strings:
        if substring in s:
            output.append(s)
    return output

