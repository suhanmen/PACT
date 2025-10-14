from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    n = len(string)
    prefixes = []
    for i in range(1, n+1):
        prefix = string[0:i]
        prefixes.append(prefix)
    return prefixes
