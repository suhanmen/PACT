Here is the Python function implemented in a markdown style code block:

```python
def get_max_sum(n):
    if n == 0:
        return 0
    else:
        return max(get_max_sum(n//2) + get_max_sum(n//3) + get_max_sum(n//4) + get_max_sum(n//5), n)

# Test the function
assert get_max_sum(60) == 106
```

This function uses recursion to calculate the maximum sum possible by using the given equation. It checks if the input `n` is 0, if so it returns 0. Otherwise, it calculates the maximum sum by recursively calling the function with `n/2`, `n/3`, `n/4`, and `n/5` and adding the results. It then compares this sum with `n` and returns the maximum of the two.

Please note that this function may not work for large inputs due to the recursion depth limit in Python. For such cases, you may need to use a different approach, such as dynamic programming.
