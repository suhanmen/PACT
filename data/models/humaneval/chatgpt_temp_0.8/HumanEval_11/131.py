from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert strings to integers
    int_a = int(a, 2)
    int_b = int(b, 2)
    
    # Perform XOR operation
    result = int_a ^ int_b
    
    # Convert result to binary string
    binary_result = bin(result)[2:]
    
    # Pad binary string with leading zeros if necessary
    padded_result = binary_result.zfill(max(len(a), len(b)))
    
    return padded_result
