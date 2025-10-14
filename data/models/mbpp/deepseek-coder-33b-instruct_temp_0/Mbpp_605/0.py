Here is the Python function to check if the given integer is a prime number:

```python
def prime_num(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# Test the function
print(prime_num(13))  # Output: True
```

This function works by checking divisibility starting from 2 up to the square root of the number. If the number is divisible by any of these, it is not a prime number. If the number is not divisible by any of these, it is a prime number. The function also handles the special cases of 2 and 3 separately.
