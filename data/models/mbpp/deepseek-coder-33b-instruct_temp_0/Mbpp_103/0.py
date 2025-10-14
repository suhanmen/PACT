Here is the Python function to find the Eulerian number a(n, m) using dynamic programming:

```python
def eulerian_num(n, m):
    if m >= n or m < 0:
        raise ValueError("m must be between 0 and n-1")

    # Initialize the DP table
    dp = [[0] * (m+2) for _ in range(n+1)]
    dp[0][0] = 1

    # Fill the DP table
    for i in range(1, n+1):
        for j in range(1, min(i, m+1)):
            dp[i][j] = (j+1)*dp[i-1][j] + (i-j+1)*dp[i-1][j-1]

    return dp[n][m]

# Test the function
assert eulerian_num(3, 1) == 4
```

This function uses a dynamic programming approach to calculate the Eulerian number. It first initializes a 2D DP table with dimensions (n+1) x (m+2), where n is the input number and m is the second input number. The DP table is filled in a bottom-up manner, with the base case being dp[0][0] = 1. The function then iterates over the DP table, filling in the remaining cells based on the recurrence relation for Eulerian numbers. The final result is the value at dp[n][m], which is the Eulerian number a(n, m).
