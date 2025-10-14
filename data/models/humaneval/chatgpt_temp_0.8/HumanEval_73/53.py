def smallest_change(arr):
    n = len(arr)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
    return dp[0][n-1]
