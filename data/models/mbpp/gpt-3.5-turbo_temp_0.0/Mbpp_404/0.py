Here is the completed code snippet:

```python
def minimum(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2

assert minimum(1, 2) == 1
```

The `minimum` function takes two numbers as input and compares them using an if-else statement. If `num1` is less than `num2`, it returns `num1`, otherwise it returns `num2`. The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `minimum(1, 2)` returns `1`.