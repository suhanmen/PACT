Here is the Python function implemented in a markdown style code block:

```python
def get_total_number_of_sequences(m, n):
    if n == 0:
        return 1
    else:
        total = 0
        for i in range(2 * n, m + 1):
            total += get_total_number_of_sequences(i, n - 1)
        return total

print(get_total_number_of_sequences(10, 4))
```

This function uses recursion to calculate the total number of sequences. It starts by checking if `n` is 0, in which case it returns 1 (since there is only one possible sequence of length 0, which is an empty sequence). If `n` is not 0, it initializes a variable `total` to 0 and then loops over all integers from `2 * n` to `m` (inclusive). For each integer `i`, it recursively calls `get_total_number_of_sequences(i, n - 1)` and adds the result to `total`. Finally, it returns `total`.

The function is then called with the arguments `10` and `4`, and the result is printed.
