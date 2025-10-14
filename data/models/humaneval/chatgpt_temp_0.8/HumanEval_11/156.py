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
    # perform XOR operation using the ^ operator
    result_int = int_a ^ int_b
    # convert the result integer back to a binary string
    result_str = bin(result_int)[2:]
    # pad the string with leading zeros if necessary
    result_str = result_str.rjust(max(len(a), len(b)), '0')
    return result_str
