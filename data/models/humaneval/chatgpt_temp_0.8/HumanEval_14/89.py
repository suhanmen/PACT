from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefix_list = []
    for i in range(1, len(string) + 1):
        prefix_list.append(string[:i])
    return prefix_list
