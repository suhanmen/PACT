Here is the completed code snippet:

```python
def is_Even(number):
    if number % 2 == 0:
        return True
    else:
        return False

assert is_Even(1) == False
```

This code defines a function `is_Even` that takes a number as input and checks if it is even or not. If the number is divisible by 2 without any remainder, it is considered even and the function returns `True`. Otherwise, it returns `False`.

The `assert` statement is used to verify that the function behaves as expected. In this case, it checks if `is_Even(1)` returns `False`, which is the expected result for an odd number.