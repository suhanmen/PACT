from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ 
    Filter an input list of strings only for ones that start with a given prefix.

    Args:
        strings: A list of strings to filter.
        prefix: A string prefix to filter by.

    Returns:
        A list of strings that start with the given prefix.
    """
    return [s for s in strings if s.startswith(prefix)]
