Here is the Python function to toggle bits of the number except the first and the last bit:

```python
def toggle_middle_bits(n):
    # Get the number of bits in the number
    bits = len(bin(n)[2:])

    # Create a mask with the first and last bit set to 1 and the rest set to 0
    mask = (1 << (bits - 1)) | (1 << 0)

    # Toggle the middle bits
    n = n ^ ((1 << (bits - 1)) - 1)

    # Set the first and last bit
    n = n | mask

    return n

print(toggle_middle_bits(9))  # Output: 15
```

This function works by first getting the number of bits in the input number. It then creates a mask with the first and last bit set to 1 and the rest set to 0. It then uses the XOR operator to toggle the middle bits of the number. Finally, it uses the OR operator to set the first and last bit of the number.
