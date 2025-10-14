Here is the Python function to solve the problem:

```python
def are_equivalent(num1, num2):
    def sum_of_divisors(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                j = i * i
                n //= i
                while n % i == 0:
                    j *= i
                    n //= i
                sum += j
                sum += n
        if n > 1:
            sum += n
        return sum

    return sum_of_divisors(num1) == sum_of_divisors(num2)
```

This function first defines a helper function `sum_of_divisors(n)` that calculates the sum of the divisors of a number `n`. It then uses this helper function to calculate the sum of the divisors of `num1` and `num2`, and checks if they are equal.

The `sum_of_divisors(n)` function works by iterating over all numbers `i` from `2` to `sqrt(n)`, and for each `i`, it checks if `i` is a divisor of `n`. If `i` is a divisor, it adds `i` to the sum, and then divides `n` by `i` until `i` is no longer a divisor. If `n` is greater than `1` after this process, it adds `n` to the sum.

The time complexity of this function is `O(sqrt(n))`, where `n` is the input number.
