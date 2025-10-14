"""
Write a python function to find whether the parity of a given number is odd.
assert find_Parity(12) == False
"""



def find_Parity(number):
    return bool(number & 1)

# Example usage:
# assert find_Parity(12) == False
