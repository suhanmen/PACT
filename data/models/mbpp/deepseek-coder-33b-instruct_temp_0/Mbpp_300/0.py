Here is the Python function to solve the problem:

```python
def count_binary_seq(n):
    # Initialize the count to 0
    count = 0

    # Iterate over all possible binary sequences of length 2n
    for i in range(2**(2*n)):
        # Convert the number to binary and pad it with zeros to make it 2n bits
        binary = bin(i)[2:].zfill(2*n)

        # Check if the sum of the first n bits is equal to the sum of the last n bits
        if binary[:n].count('1') == binary[n:].count('1'):
            count += 1

    return count
```

This function works by iterating over all possible binary sequences of length 2n, converting each number to binary, and then checking if the sum of the first n bits is equal to the sum of the last n bits. If it is, it increments the count.

Please note that this function will not work for large values of n due to the time complexity of the function. For large values of n, you may need to use a more efficient algorithm or data structure.
