from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # Convert string inputs into integer lists
    a_list = [int(char) for char in a]
    b_list = [int(char) for char in b]
    
    # Create a new list to store the XOR results
    result = []
    
    # XOR each element in the two lists and append the result to the new list
    for i in range(len(a_list)):
        result.append(a_list[i] ^ b_list[i])
    
    # Convert the result list back to a string
    result_string = ''.join([str(char) for char in result])
    
    return result_string
