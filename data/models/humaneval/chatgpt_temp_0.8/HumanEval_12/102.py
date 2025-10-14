python
from typing import List, Optional


def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_len = 0
    longest_str = ""
    for s in strings:
        if len(s) > max_len:
            max_len = len(s)
            longest_str = s
    for s in strings:
        if len(s) == max_len and s != longest_str:
            return longest_str
    return longest_str
