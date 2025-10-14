Sure, here is the Python function to find nth Bell number:

```python
def bell_Number(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        bell[i][0] = bell[i-1][i-1]
        for j in range(1, i+1):
            bell[i][j] = bell[i-1][j-1] + bell[i][j-1]
    return bell[n][0]

# Test the function
print(bell_Number(2))  # Output: 2
```

This function uses dynamic programming to calculate the Bell numbers. The Bell number is the number of ways to partition a set. The function first initializes a 2D array `bell` with all elements set to 0. The first element of the first row is set to 1. Then, for each row `i` from 1 to `n`, the first element of the row is set to the last element of the previous row. For each element in the row, it is set to the sum of the previous element in the row and the previous element in the previous row. Finally, the function returns the first element of the last row, which is the nth Bell number.
