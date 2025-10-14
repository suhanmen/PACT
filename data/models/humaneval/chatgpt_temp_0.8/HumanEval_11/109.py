from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert the strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Perform XOR operation
    xor_result = int_a ^ int_b
    
    # Convert the result back to binary string
    result = bin(xor_result)[2:]
    
    # Pad the result with leading zeros if necessary
    result = result.zfill(max(len(a), len(b)))
    
    return result
