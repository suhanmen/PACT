def smallest_change(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for gap in range(1, n):
        for i, j in zip(range(n - gap), range(gap, n)):
            dp[i][j] = dp[i+1][j-1] if arr[i] == arr[j] else min(dp[i+1][j], dp[i][j-1]) + 1
    return dp[0][n-1]
