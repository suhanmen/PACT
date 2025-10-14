Here is the completed code snippet:

```python
def sum_common_divisors(num1, num2):
    common_divisors = []
    for i in range(1, min(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            common_divisors.append(i)
    return sum(common_divisors)

assert sum_common_divisors(10, 15) == 6
```

In this code, we define a function `sum_common_divisors` that takes two numbers as input (`num1` and `num2`). We initialize an empty list `common_divisors` to store the common divisors of the two numbers.

We then iterate through the range from 1 to the minimum of `num1` and `num2` (inclusive) using a for loop. For each number `i` in this range, we check if it is a divisor of both `num1` and `num2` by checking if the remainder of the division is 0 for both numbers. If it is, we append it to the `common_divisors` list.

Finally, we return the sum of the `common_divisors` list using the `sum()` function.

The `assert` statement at the end of the code snippet checks if the function returns the expected result for the given example (10 and 15), which is 6.