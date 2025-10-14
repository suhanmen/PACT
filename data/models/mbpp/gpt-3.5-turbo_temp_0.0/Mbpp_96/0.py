Here's the completed code snippet:

```python
def divisor(n):
    count = 0
    for i in range(1, n+1):
        if n % i == 0:
            count += 1
    return count

assert divisor(15) == 4
```

The `divisor` function takes an integer `n` as input and initializes a variable `count` to keep track of the number of divisors. It then iterates through all numbers from 1 to `n` and checks if `n` is divisible by each number. If it is, the `count` is incremented by 1. Finally, the function returns the `count`.

The `assert` statement is used to verify that the function returns the expected result for the given test case. In this case, it checks if `divisor(15)` returns 4, which is the correct number of divisors for the number 15.