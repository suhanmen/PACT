Here is the completed code snippet:

```python
def round_and_sum(numbers):
    total_sum = 0
    for num in numbers:
        total_sum += round(num)
    return total_sum * len(numbers)

assert round_and_sum([22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]) == 243
```

The function `round_and_sum` takes a list of numbers as input. It initializes a variable `total_sum` to 0. Then, it iterates over each number in the input list and adds the rounded value of each number to `total_sum`. Finally, it returns the product of `total_sum` and the length of the input list.

The `assert` statement at the end of the code snippet verifies that the function produces the expected result for the given example input.