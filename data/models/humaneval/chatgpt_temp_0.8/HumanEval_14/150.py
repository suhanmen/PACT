from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    if not string:
        return []
    prefixes = [string[0]]
    for i in range(1, len(string)):
        prefixes.append(prefixes[i-1] + string[i])
    return prefixes
