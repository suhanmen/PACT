from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert the input strings to integer values
    a_val = int(a, 2)
    b_val = int(b, 2)

    # Perform the XOR operation
    result = a_val ^ b_val

    # Convert the result back to a binary string and remove the '0b' prefix
    return bin(result)[2:]
