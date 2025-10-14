from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix. """
    filtered_list = []
    for string in strings:
        if string.startswith(prefix):
            filtered_list.append(string)
    return filtered_list
