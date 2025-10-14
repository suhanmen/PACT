from typing import List

def all_prefixes(string: str) -> List[str]:
    """
    Return a list of all prefixes from shortest to longest of the given string.

    :param string: The input string for which prefixes are to be found.
    :return: A list containing all prefixes of the input string in order of length, from shortest to longest.
    """
    prefixes = []
    for i in range(len(string)):
        prefixes.append(string[:i+1])
    return prefixes
