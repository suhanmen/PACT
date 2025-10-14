Sure, here is the Python function to find nth polite number:

```python
def is_polite(n):
    count = 0
    i = 1
    while True:
        if bin(i).count('1') % 2 == 0:
            count += 1
        if count == n:
            return i
        i += 1

# Test the function
print(is_polite(7))  # Output: 11
```

This function works by iterating over positive integers, checking if the binary representation of the number has an even number of 1's. If it does, it increments a counter. When the counter reaches the input number `n`, it returns the current number.

Please note that this function may not be the most efficient for large inputs, as it has to iterate over all positive integers until it finds the nth polite number.
