def smallest_change(arr):
    n = len(arr)
    # initialize the dynamic programming table
    dp = [[0] * n for _ in range(n)]
    # fill in the table diagonally
    for k in range(n):
        for i, j in zip(range(n - k), range(k, n)):
            if i == j:
                dp[i][j] = 0
            elif arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
    return dp[0][n-1]
