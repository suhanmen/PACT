from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Pad the shorter string with leading zeros if necessary
    if len(a) < len(b):
        a = '0' * (len(b) - len(a)) + a
    elif len(b) < len(a):
        b = '0' * (len(a) - len(b)) + b

    # Perform XOR on each corresponding bit and build the result string
    result = ''
    for i in range(len(a)):
        if a[i] == b[i]:
            result += '0'
        else:
            result += '1'

    return result
