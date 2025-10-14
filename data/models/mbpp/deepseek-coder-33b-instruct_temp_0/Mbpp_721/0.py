Here is a Python solution using dynamic programming:

```python
def maxAverageOfPath(matrix):
    n = len(matrix)
    dp = [[0.0]*n for _ in range(n)]
    dp[0][0] = float(matrix[0][0])

    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + matrix[i][0]
        dp[0][i] = dp[0][i-1] + matrix[0][i]

    for i in range(1, n):
        for j in range(1, n):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]

    return dp[-1][-1] / (2*n - 1)

print(maxAverageOfPath([[1, 2, 3], [6, 5, 4], [7, 3, 9]]))
```

This solution works by initializing a dynamic programming (dp) table with the same dimensions as the input matrix. The dp table is filled in a bottom-up manner, where each cell (i, j) is the maximum average path that can be obtained by reaching cell (i, j) from the top-left cell. The maximum average path to reach cell (i, j) is the maximum of the maximum average path to reach cell (i-1, j) and cell (i, j-1), plus the cost of cell (i, j). The maximum average path to reach the bottom-right cell is then the value in the bottom-right cell of the dp table, divided by the total number of cells in the path (which is 2*n - 1).
