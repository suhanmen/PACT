Here is the completed code snippet:

```python
def maxAverageOfPath(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    # Create a 2D array to store the maximum average at each cell
    dp = [[0] * m for _ in range(n)]
    
    # Initialize the first cell with its own value
    dp[0][0] = matrix[0][0]
    
    # Calculate the maximum average for each cell
    for i in range(n):
        for j in range(m):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                dp[i][j] = dp[i][j-1] + matrix[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + matrix[i][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + matrix[i][j]
    
    # Calculate the maximum average over all paths
    return dp[n-1][m-1] / (n + m - 1)
```

The code uses dynamic programming to calculate the maximum average at each cell. It starts from the top-left cell and iterates through each cell, calculating the maximum average by considering the previous cells. Finally, it returns the maximum average over all paths, which is the value at the bottom-right cell divided by the total number of cells visited in the path.