Here is the Python function to check whether the given number can be represented as the difference of two squares or not.

```python
def dif_Square(n):
    i = 1
    while i * i <= n:
        j = 1
        while j * j <= i * i:
            if i * i - j * j == n:
                return True
            j += 1
        i += 1
    return False
```

This function works by iterating over all possible pairs of squares (i, j) where i^2 - j^2. If it finds a pair where the difference equals the input number, it returns True. If it iterates over all possible pairs without finding a match, it returns False.

You can test the function with the following code:

```python
print(dif_Square(5))  # Output: True
```
