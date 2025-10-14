Here is the Python function implemented in a markdown style code block:

```python
def sum_negativenum(numbers):
    """
    Write a function to calculate the sum of the negative numbers of a given list of numbers.
    """
    return sum(num for num in numbers if num < 0)

# Test the function
assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==-32
```

This function uses a generator expression to iterate over the numbers in the list and only include the negative numbers. The built-in `sum` function is then used to calculate the sum of these numbers. The `assert` statement is used to test the function with the provided example.
