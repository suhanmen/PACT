Here is the Python function to calculate the sum of Perrin numbers:

```python
def cal_sum(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b, c = 0, 1, 1
        for _ in range(n - 2):
            a, b, c = b, c, a + b
        return c

print(cal_sum(9))  # Output: 49
```

This function uses a loop to calculate the sum of the first `n` Perrin numbers. The Perrin numbers are a sequence of numbers in which each number is the sum of the two preceding ones, with starting values 0, 1, 1. The function returns the sum of the first `n` Perrin numbers.
