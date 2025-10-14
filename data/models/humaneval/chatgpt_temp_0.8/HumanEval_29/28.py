python
from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix."""
    prefix_len = len(prefix)
    return [s for s in strings if s[:prefix_len] == prefix]
