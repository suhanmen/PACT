"""
Write a python function to check whether the two numbers differ at one bit position only or not.
assert differ_At_One_Bit_Pos(13,9) == True
"""



def differ_At_One_Bit_Pos(a, b):
    # XOR of two numbers will have set bits only at positions where
    # the two numbers differ
    xor_result = a ^ b
    
    # Check if XOR result is a power of two, which means only one bit is different
    return (xor_result & (xor_result - 1)) == 0 and xor_result != 0

# Example usage
# assert differ_At_One_Bit_Pos(13,9) == True
