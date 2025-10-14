def smallest_change(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for j in range(1, n):
        for i in range(j-1, -1, -1):
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]
