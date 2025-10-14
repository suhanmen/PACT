Here is the Python function to check whether the given number is even or not:

```python
def is_Even(n):
    if n % 2 == 0:
        return True
    else:
        return False
```

You can test the function with the following code:

```python
assert is_Even(1) == False
```

This function works by using the modulus operator (%) to find the remainder of the division of the input number by 2. If the remainder is 0, the number is even and the function returns True. If the remainder is not 0, the number is odd and the function returns False.
