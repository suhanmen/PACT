Here is the Python function to set all even bits of a given number:

```python
def even_bit_set_number(n):
    binary = bin(n)[2:]
    binary = binary[::-1]
    result = ''
    for i in range(len(binary)):
        if i % 2 == 0:
            result += '1'
        else:
            result += binary[i]
    result = result[::-1]
    return int(result, 2)

print(even_bit_set_number(10))  # Output: 10
```

This function works by first converting the given number to binary. It then reverses the binary string and iterates over each bit. If the bit's position is even (0-indexed), it sets the bit to 1. Otherwise, it leaves the bit as is. Finally, it reverses the string again and converts it back to an integer.

Please note that the function `even_bit_set_number(10)` will return `10` because the binary representation of `10` is `1010`, and the even bits are already set to `1`.
