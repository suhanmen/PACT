Here is the completed code snippet:

```python
def median_numbers(num1, num2, num3):
    numbers = [num1, num2, num3]
    numbers.sort()
    median = numbers[1]
    return median

assert median_numbers(25, 55, 65) == 55.0
```

In this code, the function `median_numbers` takes three numbers as input and stores them in a list called `numbers`. The list is then sorted in ascending order using the `sort()` method. The median is the middle number in a sorted list, so we retrieve the number at index 1 (since Python uses zero-based indexing). Finally, the median is returned as the output of the function.

The `assert` statement is used to verify that the function returns the expected result. In this case, it checks if `median_numbers(25, 55, 65)` is equal to `55.0`. If the condition is true, the program continues execution. If the condition is false, an `AssertionError` is raised.