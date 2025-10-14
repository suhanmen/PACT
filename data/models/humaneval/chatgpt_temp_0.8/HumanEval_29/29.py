from typing import List


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    result = []
    for s in strings:
        if s.startswith(prefix):
            result.append(s)
    return result
