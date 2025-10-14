Here's the completed code snippet:

```python
def toggle_middle_bits(num):
    # Convert the number to binary representation
    binary = bin(num)[2:]

    # Toggle the bits except the first and last bit
    toggled = '1' + ''.join(['0' if bit == '1' else '1' for bit in binary[1:-1]]) + '1'

    # Convert the toggled binary back to decimal
    return int(toggled, 2)

assert toggle_middle_bits(9) == 15
```

In this code, we first convert the given number to its binary representation using the `bin()` function. Then, we toggle the bits except the first and last bit by iterating over the binary string and replacing each bit with its opposite (0 becomes 1 and 1 becomes 0). Finally, we convert the toggled binary back to decimal using the `int()` function with base 2.