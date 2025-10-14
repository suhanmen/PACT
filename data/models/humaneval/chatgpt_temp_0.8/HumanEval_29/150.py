from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """
    Filter an input list of strings only for ones that start with a given prefix.

    :param strings: the list of strings to filter
    :param prefix: the prefix to filter by
    :return: a list of strings that start with the given prefix
    """
    filtered_strings = []
    for s in strings:
        if s.startswith(prefix):
            filtered_strings.append(s)
    return filtered_strings
