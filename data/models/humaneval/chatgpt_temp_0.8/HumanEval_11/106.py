from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert the strings to integers first
    a_int = int(a, 2)
    b_int = int(b, 2)
    
    # Perform the XOR operation
    result_int = a_int ^ b_int
    
    # Convert the result back to a string
    result_str = format(result_int, 'b')
    
    return result_str
