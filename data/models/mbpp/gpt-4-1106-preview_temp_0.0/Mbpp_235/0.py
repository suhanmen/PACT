"""
Write a python function to set all even bits of a given number.
assert even_bit_set_number(10) == 10
"""



def even_bit_set_number(n):
    # Iterate through all bits of the number
    for i in range(0, 32, 2):  # Considering a 32-bit integer
        # Set the even bit (0, 2, 4, ...) by using the OR operator with 1 shifted to the i-th position
        n |= (1 << i)
    return n

# Example usage
# The binary representation of 10 is 1010
# Setting all even bits, we get 1010 (since the even bits are already set in this case)
assert even_bit_set_number(10) == 10
