from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # If the lengths of the two strings are different, we cannot perform XOR.
    if len(a) != len(b):
        raise ValueError("Input strings must be of the same length")

    # Define an empty string to store the result of the XOR operation.
    result = ""

    # Iterate over the characters of the two input strings.
    for i in range(len(a)):
        # If the corresponding characters are the same, append '0' to the result.
        if a[i] == b[i]:
            result += '0'
        # Otherwise, append '1' to the result.
        else:
            result += '1'

    return result
