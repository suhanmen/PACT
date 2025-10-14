from typing import List


def concatenate(strings: List[str]) -> str:
    """ Concatenate list of strings into a single string
    >>> concatenate([])
    ''
    >>> concatenate(['a', 'b', 'c'])
    'abc'
    """
    # initialize empty string
    result = ''
    # loop through each string in the list
    for string in strings:
        # add the string to the result
        result += string
    # return the concatenated string
    return result
