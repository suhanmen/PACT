from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert strings to binary integers
    int_a = int(a, 2)
    int_b = int(b, 2)

    # Use XOR operator on binary integers
    int_result = int_a ^ int_b

    # Convert result back to binary string
    str_result = bin(int_result)[2:]

    # Pad string with leading zeros if necessary
    if len(str_result) < len(a):
        str_result = '0' * (len(a) - len(str_result)) + str_result

    return str_result
