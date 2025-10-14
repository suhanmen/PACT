from typing import List

def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Check if the strings are of equal length
    if len(a) != len(b):
        return "Error: Both strings should be of equal length."

    # Initialize the result string
    result = ""

    # Perform XOR operation on each bit of the input strings
    for i in range(len(a)):
        # If both bits are same, then XOR result is 0, else 1
        if a[i] == b[i]:
            result += "0"
        else:
            result += "1"

    return result
