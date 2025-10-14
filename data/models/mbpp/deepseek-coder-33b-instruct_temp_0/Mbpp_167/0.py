Here is the Python function to find the smallest power of 2 greater than or equal to n:

```python
def next_power_of_2(n):
    res = 1
    if n == 0:
        return 1
    while res <= n:
        res = res << 1
    return res
```

This function uses bitwise shift operation to find the next power of 2. It starts with `res` as 1 and keeps shifting it to the left until it is greater than or equal to `n`. The final result is the smallest power of 2 greater than or equal to `n`.
