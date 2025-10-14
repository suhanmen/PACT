def smallest_change(arr):
    n = len(arr)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(i - 1, -1, -1):
            if arr[i] == arr[j]:
                dp[i][j] = dp[i - 1][j + 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j + 1]) + 1
    return dp[-1][0]
