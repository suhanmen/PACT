"""
Write a python function to set the left most unset bit.
assert set_left_most_unset_bit(10) == 14
"""



def set_left_most_unset_bit(n):
    if n == 0:
        return 1
    m = n
    mask = 1
    # Find the leftmost unset bit
    while m & mask:
        mask = mask << 1
    # Set the leftmost unset bit
    return n | mask


assert set_left_most_unset_bit(10) == 14
