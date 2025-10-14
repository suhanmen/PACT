from typing import List


def all_prefixes(string: str) -> List[str]:
    """Return list of all prefixes from shortest to longest of the input string"""
    result = []
    for i in range(len(string)):
        result.append(string[:i+1])
    return result

