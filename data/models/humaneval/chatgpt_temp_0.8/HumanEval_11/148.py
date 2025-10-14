from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert strings to integers (base 2)
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # perform XOR operation and convert back to binary string
    result = bin(int_a ^ int_b)[2:]
    
    # pad with leading 0s if needed
    result = result.zfill(max(len(a), len(b)))
    
    return result
