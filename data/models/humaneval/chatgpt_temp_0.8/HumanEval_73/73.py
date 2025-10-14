def smallest_change(arr):
    n = len(arr)
    # Initialize a 2D table to store the minimum number of changes needed
    # to make any subarray from i to j (inclusive) palindromic
    dp = [[0] * n for _ in range(n)]

    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if arr[i] == arr[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i][j - 1], dp[i + 1][j]) + 1

    return dp[0][n - 1]
