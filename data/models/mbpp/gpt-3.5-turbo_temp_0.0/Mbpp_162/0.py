Here's the completed code snippet:

```python
def sum_series(n):
    total = 0
    for i in range(n // 2 + 1):
        total += n - 2 * i
    return total

assert sum_series(6) == 12
```

In this code, we define a function `sum_series` that takes an integer `n` as input. We initialize a variable `total` to keep track of the sum. 

We then use a for loop to iterate from `i=0` to `n // 2`. In each iteration, we calculate `n - 2 * i` and add it to the `total`. 

Finally, we return the `total` as the result of the function. The `assert` statement is used to verify that the function returns the expected result for the given input.