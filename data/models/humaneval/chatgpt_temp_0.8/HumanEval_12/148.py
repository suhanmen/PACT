from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    if not strings:
        return None
    max_str = strings[0]
    for s in strings:
        if len(s) > len(max_str):
            max_str = s
    return max_str
