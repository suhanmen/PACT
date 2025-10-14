Here is the Python function to find the number of ways to partition a set of Bell numbers.

```python
def bell_number(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]

print(bell_number(2))
```

This function uses dynamic programming to calculate the Bell numbers. The Bell number B(n) is the number of ways to partition a set of n distinct items. The function first initializes a 2D array `bell` with all elements set to 0. The base case is when `n=0`, the Bell number is 1. Then, for each `i` from 1 to `n`, the function calculates the Bell number by summing up the previous Bell number and the Bell number of the previous row. The final result is the Bell number of the input `n`.
