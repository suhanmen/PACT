Here is the Python function to calculate the nth Catalan number:

```python
def catalan_number(n):
    if n <=1 :
        return 1
    res = 0
    for i in range(n):
        res += catalan_number(i) * catalan_number(n-i-1)
    return res

# Test the function
print(catalan_number(10))  # Output: 16796
```

This function uses a recursive approach to calculate the Catalan numbers. It starts by checking if `n` is less than or equal to 1, in which case it returns 1. If `n` is greater than 1, it calculates the Catalan number by summing the product of the Catalan numbers of `i` and `n-i-1` for all `i` from 0 to `n-1`.

Please note that this function is not efficient for large values of `n` because it performs a lot of redundant calculations. A more efficient approach would be to use dynamic programming to store previously calculated Catalan numbers.
