from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    prefixes = []
    # loop through the input string
    for i in range(len(string)):
        # add the substring from the beginning up to the current index to the prefixes list
        prefixes.append(string[:i+1])
    return prefixes
