Here is the completed code snippet:

```python
def power_base_sum(base, power):
    result = base ** power
    digit_sum = sum(int(digit) for digit in str(result))
    return digit_sum

assert power_base_sum(2, 100) == 115
```

In this code, the `power_base_sum` function takes two arguments: `base` and `power`. It calculates the result of raising the `base` to the `power` using the exponentiation operator `**`. Then, it converts the result to a string and iterates over each digit using a list comprehension. Each digit is converted back to an integer using the `int` function, and the sum of all the digits is calculated using the `sum` function. Finally, the function returns the digit sum.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `power_base_sum(2, 100)` is equal to 115. If the assertion fails, an `AssertionError` will be raised.