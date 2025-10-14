def smallest_change(arr):
    n = len(arr)
    # Initialize a dynamic programming table of size n x n
    dp = [[0] * n for _ in range(n)]
    # Fill in the base cases (single elements are palindromic)
    for i in range(n):
        dp[i][i] = 0
    # Fill in the rest of the table bottom-up
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])
    # The result is the minimum number of changes to make the whole array palindromic
    return dp[0][n-1]
