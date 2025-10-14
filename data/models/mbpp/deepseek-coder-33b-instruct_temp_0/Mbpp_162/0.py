Here is the Python function implemented in a markdown style code block:

```python
def sum_series(n):
    sum = 0
    for i in range(n // 2 + 1):
        sum += n - 2 * i
    return sum

# Test the function
assert sum_series(6) == 12
```

This function calculates the sum of the series (n - 2*i) from i=0 to n // 2. It uses a for loop to iterate over the range of i values, and for each i, it adds the value of (n - 2*i) to the sum. The function finally returns the calculated sum.
