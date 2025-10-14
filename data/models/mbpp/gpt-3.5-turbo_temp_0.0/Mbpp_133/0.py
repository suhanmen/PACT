Here is the completed code snippet:

```python
def sum_negativenum(numbers):
    sum_negative = 0
    for num in numbers:
        if num < 0:
            sum_negative += num
    return sum_negative

assert sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]) == -32
```

The function `sum_negativenum` takes a list of numbers as input and initializes a variable `sum_negative` to 0. It then iterates over each number in the list and checks if it is less than 0. If it is, the number is added to `sum_negative`. Finally, the function returns the sum of the negative numbers.

The `assert` statement at the end of the code snippet checks if the function returns the expected result for the given input list. If the assertion fails, an error will be raised.