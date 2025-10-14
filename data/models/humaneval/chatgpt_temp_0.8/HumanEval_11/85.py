from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert the input strings to integers
    a_int = int(a, 2)
    b_int = int(b, 2)
    
    # perform XOR operation on the integers
    result_int = a_int ^ b_int
    
    # convert the result back to a binary string
    result_str = bin(result_int)[2:]
    
    # pad the result string with leading zeros if necessary
    max_len = max(len(a), len(b))
    result_str = result_str.zfill(max_len)
    
    return result_str
