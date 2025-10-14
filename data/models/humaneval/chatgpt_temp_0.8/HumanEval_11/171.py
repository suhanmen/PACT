from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert the input strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)

    # Perform the XOR operation on the integers
    result_int = int_a ^ int_b

    # Convert the result back to a binary string
    result_str = bin(result_int)[2:]

    # Pad the result string with leading zeros if necessary
    padding = max(len(a), len(b)) - len(result_str)
    if padding > 0:
        result_str = '0' * padding + result_str

    return result_str
