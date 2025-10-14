from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert strings to binary numbers
    num_a = int(a, 2)
    num_b = int(b, 2)
    
    # Perform XOR
    result = num_a ^ num_b
    
    # Convert result back to binary string
    return "{0:b}".format(result)
