from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    """
    filtered_strings = []
    for string in strings:
        if string.startswith(prefix):
            filtered_strings.append(string)
    return filtered_strings
