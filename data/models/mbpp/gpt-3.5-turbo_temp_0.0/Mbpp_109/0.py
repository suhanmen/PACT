Here is the completed code snippet:

```python
def odd_equivalent(binary_string, num_rotations):
    count = 0
    for _ in range(num_rotations):
        if int(binary_string, 2) % 2 != 0:
            count += 1
        binary_string = binary_string[-1] + binary_string[:-1]
    return count

assert odd_equivalent("011001", 6) == 3
```

In this code, the `odd_equivalent` function takes in a binary string and the number of rotations as parameters. It initializes a count variable to keep track of the number of numbers with an odd value.

The function then loops `num_rotations` times. In each iteration, it checks if the decimal value of the binary string (obtained using `int(binary_string, 2)`) is odd. If it is, the count is incremented.

After each iteration, the binary string is rotated by moving the last character to the front (`binary_string[-1] + binary_string[:-1]`).

Finally, the function returns the count.

The `assert` statement at the end verifies that the function returns the expected result for the given example.