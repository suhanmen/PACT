def smallest_change(arr):
    n = len(arr)
    # Create a 2D list to store the minimum number of changes required to make
    # the subarray arr[i:j+1] palindromic.
    dp = [[0] * n for _ in range(n)]
    # Base case: a subarray of length 1 is already palindromic.
    for i in range(n):
        dp[i][i] = 0

    # Fill in the dynamic programming table from bottom up.
    for k in range(1, n):
        for i in range(n - k):
            j = i + k
            if arr[i] == arr[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = 1 + min(dp[i+1][j], dp[i][j-1])

    # The minimum number of changes required to make the whole array palindromic
    # is the value in the top-right corner of the table.
    return dp[0][n-1]
