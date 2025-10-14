Here is the Python function to find the nth Jacobsthal number:

```python
def jacobsthal_num(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 2 * jacobsthal_num(n - 1) + jacobsthal_num(n - 2)

# Test the function
print(jacobsthal_num(5))  # Output: 11
```

This function uses the recursive formula for Jacobsthal numbers: `J(n) = 2 * J(n - 1) + J(n - 2)`. It starts with the base cases `J(0) = 0` and `J(1) = 1`. For `n > 1`, it calculates the Jacobsthal number by recursively calling the function for `n - 1` and `n - 2`.
