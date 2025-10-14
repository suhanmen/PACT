Here is the completed code snippet:

```python
def find_Parity(number):
    if number % 2 == 0:
        return False
    else:
        return True

assert find_Parity(12) == False
```

In this code, the function `find_Parity` takes a number as input and checks if it is divisible by 2. If the number is divisible by 2, it returns `False` indicating that the parity is even. Otherwise, it returns `True` indicating that the parity is odd. The `assert` statement is used to verify that the function returns the expected result for the given test case.