Here is the Python function to find the number of divisors of a given integer:

```python
def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# Test the function
assert divisor(15) == 4
```

This function works by iterating over all numbers from 1 to the given integer `n`. If `n` is divisible by the current number `i`, it increments the `count` variable. At the end of the function, it returns the `count`, which represents the number of divisors of `n`.
