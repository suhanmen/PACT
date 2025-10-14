Here is the completed code snippet:

```python
def maximum(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

assert maximum(5, 10) == 10
```

The `maximum` function takes in two numbers, `num1` and `num2`, and compares them using an `if` statement. If `num1` is greater than `num2`, it returns `num1`, otherwise it returns `num2`. The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `maximum(5, 10)` is equal to `10`.