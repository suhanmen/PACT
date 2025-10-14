from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert the input strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    # perform XOR operation
    result = int_a ^ int_b
    # convert the result back to a binary string and return it
    return "{0:b}".format(result)
