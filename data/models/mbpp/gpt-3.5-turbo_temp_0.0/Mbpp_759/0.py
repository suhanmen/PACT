Here is the completed code snippet:

```python
def is_decimal(string):
    try:
        number = float(string)
        if round(number, 2) == number:
            return True
        else:
            return False
    except ValueError:
        return False

assert is_decimal('123.11') == True
```

In this code, the `is_decimal` function takes a string as input and attempts to convert it to a float using the `float()` function. If the conversion is successful, it checks if the rounded value of the number is equal to the original number. If they are equal, it returns `True`, indicating that the string is a decimal number with a precision of 2. If the conversion fails or the rounded value is not equal to the original number, it returns `False`.

The `assert` statement at the end of the code snippet checks if the `is_decimal` function returns `True` for the given test case `'123.11'`. If the function returns `True`, the assertion passes and the code continues execution. If the function returns `False`, an `AssertionError` is raised, indicating that the function is not working correctly.