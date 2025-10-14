Here is the completed code snippet:

```python
def bell_number(n):
    bell = [[0 for j in range(n+1)] for i in range(n+1)]
    bell[0][0] = 1

    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]

        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]

    return bell[n][0]

assert bell_number(2) == 2
```

The function `bell_number` takes an integer `n` as input and returns the nth Bell number. It uses a dynamic programming approach to calculate the Bell numbers. The assertion at the end checks if the function returns the correct value for `n=2`.