from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_len = max(len(s) for s in strings)
    for s in strings:
        if len(s) == max_len:
            return s
