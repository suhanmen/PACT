def smallest_change(arr):
    n = len(arr)
    # Initialize a 2D array dp with zeros
    dp = [[0] * n for _ in range(n)]
    # Fill in the diagonal with ones
    for i in range(n):
        dp[i][i] = 1
    # Fill in the upper triangle of the matrix
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i][j-1], dp[i+1][j])
    # The minimum number of changes is dp[0][n-1]
    return dp[0][n-1]
