Here is the completed code snippet:

```python
def sum_in_range(l, r):
    total = 0
    for num in range(l, r+1):
        if num % 2 != 0:
            total += num
    return total

assert sum_in_range(2, 5) == 8
```

The `sum_in_range` function takes two parameters `l` and `r`, which represent the lower and upper bounds of the range, respectively. It initializes a variable `total` to 0 to keep track of the sum of odd numbers.

The function then iterates over each number in the range from `l` to `r+1` using a for loop. If the number is odd (i.e., not divisible by 2), it adds it to the `total` variable.

Finally, the function returns the `total` sum.

The `assert` statement at the end of the code snippet checks if the function returns the expected result for the given example.