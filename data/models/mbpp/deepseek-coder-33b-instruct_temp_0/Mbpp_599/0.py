Here is the Python function implemented in a markdown style code block:

```python
def sum_average(n):
    sum_n = n * (n + 1) // 2
    avg_n = sum_n / n
    return sum_n, avg_n

# Test the function
assert sum_average(10)==(55, 5.5)
```

In this function, we first calculate the sum of the first n natural numbers using the formula `n * (n + 1) // 2`. Then, we calculate the average by dividing the sum by n. The function returns a tuple containing the sum and average.
