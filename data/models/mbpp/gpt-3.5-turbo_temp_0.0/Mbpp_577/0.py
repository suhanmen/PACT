Here's the completed code snippet:

```python
def last_Digit_Factorial(n):
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    last_digit = factorial % 10
    return last_digit

assert last_Digit_Factorial(4) == 4
```

In this code, we define a function `last_Digit_Factorial` that takes an integer `n` as input. We initialize a variable `factorial` to 1, and then use a for loop to calculate the factorial of `n`. We then use the modulo operator `%` to find the remainder when dividing the factorial by 10, which gives us the last digit. Finally, we return the last digit.

The `assert` statement at the end is used to check if the function returns the expected result. In this case, it checks if `last_Digit_Factorial(4)` returns 4. If the assertion fails, it will raise an `AssertionError`.