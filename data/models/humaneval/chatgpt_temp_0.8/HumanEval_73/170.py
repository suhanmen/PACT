def smallest_change(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]
