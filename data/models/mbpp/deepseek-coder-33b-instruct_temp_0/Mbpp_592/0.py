Here is the Python function to find the sum of the product of consecutive binomial coefficients:

```python
import math

def sum_Of_product(n):
    sum = 0
    for i in range(n):
        sum += math.comb(n, i) * math.comb(n, i+1)
    return sum
```

This function uses the `math.comb(n, k)` function to calculate the binomial coefficient, which is the number of ways to choose `k` items from `n` items without regard to the order of selection. The function then calculates the product of consecutive binomial coefficients and adds them to the sum.

Please note that the `math.comb(n, k)` function is available from Python 3.8 onwards. If you are using an earlier version of Python, you can use the following function to calculate binomial coefficients:

```python
def binomial_coefficient(n, k):
    return math.factorial(n) / (math.factorial(k) * math.factorial(n - k))
```

And then modify the `sum_Of_product` function to use this function:

```python
def sum_Of_product(n):
    sum = 0
    for i in range(n):
        sum += binomial_coefficient(n, i) * binomial_coefficient(n, i+1)
    return sum
```
