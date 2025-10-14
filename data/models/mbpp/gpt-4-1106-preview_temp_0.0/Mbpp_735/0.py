"""
Write a python function to toggle bits of the number except the first and the last bit. https://www.geeksforgeeks.org/toggle-bits-number-expect-first-last-bits/
assert toggle_middle_bits(9) == 15
"""



def toggle_middle_bits(n):
    # Calculate the number of bits in the number
    num_bits = n.bit_length()

    # Create a mask to toggle all bits except the first and the last
    # For example, if num_bits = 4, mask will be 0110
    mask = (1 << (num_bits - 2)) - 1

    # Toggle the middle bits
    result = n ^ mask

    # Ensure the first and last bits remain unchanged
    first_bit = (n >> (num_bits - 1)) & 1
    last_bit = n & 1
    result = (first_bit << (num_bits - 1)) | (result & mask) | last_bit

    return result


# Example usage
assert toggle_middle_bits(9) == 15
