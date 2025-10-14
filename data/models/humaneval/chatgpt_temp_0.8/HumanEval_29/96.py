from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    """
    filtered_list = [s for s in strings if s.startswith(prefix)]
    return filtered_list
