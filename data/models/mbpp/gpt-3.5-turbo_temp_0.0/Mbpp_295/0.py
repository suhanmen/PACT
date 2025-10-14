Here is the completed code snippet:

```python
def sum_div(num):
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    return sum(divisors)

assert sum_div(8) == 7
```

In this code, the `sum_div` function takes a number `num` as input and initializes an empty list `divisors` to store the divisors of `num`. It then iterates through all numbers from 1 to `num-1` using a for loop. If `num` is divisible by the current number `i`, it means `i` is a divisor of `num`, so it is appended to the `divisors` list. Finally, the function returns the sum of all the divisors using the `sum` function.

The `assert` statement at the end of the code snippet checks if the function returns the expected result for the given example. If the condition is true, it does nothing. If the condition is false, it raises an `AssertionError` with an optional error message.