from typing import List


def string_xor(a: str, b: str) -> str:
    """ Input are two strings a and b consisting only of 1s and 0s.
    Perform binary XOR on these inputs and return result also as a string.
    >>> string_xor('010', '110')
    '100'
    """
    # convert input strings to lists of integers
    a_list = [int(char) for char in a]
    b_list = [int(char) for char in b]

    # perform XOR operation
    result_list = [(a_list[i] + b_list[i]) % 2 for i in range(len(a_list))]

    # convert result to string
    result_string = ''.join([str(bit) for bit in result_list])

    return result_string
