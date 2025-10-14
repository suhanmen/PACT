def smallest_change(arr):
    n = len(arr)
    # initialize memoization table
    memo = [[None] * n for _ in range(n)]

    def dp(i, j):
        if i >= j:
            return 0
        if memo[i][j] is not None:
            return memo[i][j]
        if arr[i] == arr[j]:
            return dp(i+1, j-1)
        else:
            memo[i][j] = 1 + min(dp(i+1, j), dp(i, j-1))
            return memo[i][j]

    return dp(0, n-1)
