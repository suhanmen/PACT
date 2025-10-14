Here is the completed code snippet:

```python
def are_equivalent(num1, num2):
    def get_divisors(n):
        divisors = []
        for i in range(1, n+1):
            if n % i == 0:
                divisors.append(i)
        return divisors

    sum1 = sum(get_divisors(num1))
    sum2 = sum(get_divisors(num2))

    return sum1 == sum2

assert are_equivalent(36, 57) == False
```

In this code, the `are_equivalent` function takes two integers as input and determines if the sum of their divisors is the same. The `get_divisors` function is a helper function that returns a list of divisors for a given number. The `sum` function is then used to calculate the sum of the divisors for each input number. Finally, the function returns `True` if the sums are equal and `False` otherwise. The provided assertion checks if the function returns `False` for the input `(36, 57)`.