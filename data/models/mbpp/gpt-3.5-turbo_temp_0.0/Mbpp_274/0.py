Here is the completed code snippet:

```python
def even_binomial_coeff_sum(n):
    def binomial_coefficient(n, k):
        if k == 0 or k == n:
            return 1
        else:
            return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

    sum = 0
    for i in range(n+1):
        if i % 2 == 0:
            sum += binomial_coefficient(n, i)
    
    return sum

assert even_binomial_coeff_sum(4) == 8
```

In this code, we define a helper function `binomial_coefficient` that calculates the binomial coefficient using recursion. Then, we iterate through the range of `n+1` and check if the index `i` is even. If it is, we calculate the binomial coefficient using the helper function and add it to the sum. Finally, we return the sum.