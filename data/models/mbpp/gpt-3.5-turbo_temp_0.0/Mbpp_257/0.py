Here is the completed code snippet:

```python
def swap_numbers(num1, num2):
    return (num2, num1)

assert swap_numbers(10, 20) == (20, 10)
```

The `swap_numbers` function takes in two numbers, `num1` and `num2`, and returns a tuple with `num2` as the first element and `num1` as the second element. The `assert` statement checks if calling `swap_numbers(10, 20)` returns the expected result `(20, 10)`.