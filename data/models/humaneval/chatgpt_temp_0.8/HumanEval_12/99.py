python
from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_len = 0
    max_string = ''
    for string in strings:
        if len(string) > max_len:
            max_len = len(string)
            max_string = string
    return max_string
