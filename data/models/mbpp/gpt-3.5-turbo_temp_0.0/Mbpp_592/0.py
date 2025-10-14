Here's the completed code snippet:

```python
def sum_Of_product(n):
    """
    This function finds the sum of the product of consecutive binomial coefficients up to the given number n.
    """
    def binomial_coefficient(n, k):
        """
        This function calculates the binomial coefficient of n and k.
        """
        if k == 0 or k == n:
            return 1
        else:
            return binomial_coefficient(n-1, k-1) + binomial_coefficient(n-1, k)

    sum_of_product = 0
    for i in range(n):
        sum_of_product += binomial_coefficient(n, i) * binomial_coefficient(n, i+1)

    return sum_of_product

assert sum_Of_product(3) == 15
```

In this code, the `sum_Of_product` function calculates the sum of the product of consecutive binomial coefficients up to the given number `n`. The `binomial_coefficient` function is a helper function that calculates the binomial coefficient of `n` and `k`. The main function uses a loop to iterate through the range of `n` and calculates the product of consecutive binomial coefficients using the helper function. Finally, the function returns the sum of the products. The `assert` statement is used to verify that the function returns the expected result for the given input.