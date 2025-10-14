"""
Write a python function to count the number of set bits (binary digits with value 1) in a given number.
assert count_Set_Bits(2) == 1
"""



def count_Set_Bits(n):
    count = 0
    while n:
        count += n & 1
        n >>= 1
    return count

# Example usage:
# assert count_Set_Bits(2) == 1
