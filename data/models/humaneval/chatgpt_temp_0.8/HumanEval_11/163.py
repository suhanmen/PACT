def string_xor(a: str, b: str) -> str:
    """
    Input are two strings a and b consisting only of 1s and 0s. Perform binary XOR on these inputs 
    and return result also as a string.
    
    Example:
    >>> string_xor('010', '110')
    '100'
    """
    # Check if length of both strings are equal
    if len(a) != len(b):
        raise ValueError("Length of both strings should be equal.")
        
    # Use list comprehension to perform XOR operation on corresponding bits of both strings
    result = [str(int(x) ^ int(y)) for x, y in zip(a, b)]
    
    # Join the list of XORed bits to form the final string
    return ''.join(result)
