Here is the completed code snippet:

```python
def get_max_sum(n):
    if n <= 1:
        return n
    
    max_sum = max(get_max_sum(n//2), get_max_sum(n//3), get_max_sum(n//4), get_max_sum(n//5), n)
    return max_sum

assert get_max_sum(60) == 106
```

In this code, the `get_max_sum` function takes an integer `n` as input and returns the maximum sum possible using the given equation `f(n) = max( (f(n/2) + f(n/3) + f(n/4) + f(n/5)), n)`.

The function uses recursion to calculate the maximum sum. If `n` is less than or equal to 1, the function returns `n` as the maximum sum. Otherwise, it calculates the maximum sum by recursively calling `get_max_sum` on `n/2`, `n/3`, `n/4`, `n/5`, and `n`, and then taking the maximum value among them.

Finally, the code includes an assertion to verify that `get_max_sum(60)` returns the expected result of `106`.